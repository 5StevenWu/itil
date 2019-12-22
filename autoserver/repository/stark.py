from stark.service.stark import site, StarkConfig, get_choice_text, Option

from repository import models
from django.shortcuts import HttpResponse, render
from django.utils.safestring import mark_safe

from django.conf.urls import url


class BusinessUnitConfig(StarkConfig):
    # 展示的字段
    list_display = [StarkConfig.display_checkbox, 'id', 'name']
    # 排序
    order_by = ['-id']
    # 搜索
    search_list = ['name']

    # 批量操作demo
    def mutli_delete(self, request):
        print(request.POST)
        return HttpResponse('删除成功')

    mutli_delete.text = '批量删除'

    action_list = [mutli_delete]

    def get_urls(self):
        urlpatterns = [
            url(r'^list/$', self.wrapper(self.changelist_view), name=self.get_list_url_name),
            url(r'^add/$', self.wrapper(self.add_view), name=self.get_add_url_name),
            url(r'^(?P<pk>\d+)/change/', self.wrapper(self.change_view), name=self.get_change_url_name),
            # url(r'^(?P<pk>\d+)/del/', self.wrapper(self.delete_view), name=self.get_del_url_name),
        ]

        extra = self.extra_url()
        if extra:
            urlpatterns.extend(extra)

        return urlpatterns

    def get_list_display(self):
        val = []
        val.extend(self.list_display)
        val.append(StarkConfig.display_edit_del('edit'))
        return val


site.register(models.BusinessUnit, BusinessUnitConfig)


class IDCConfig(StarkConfig):
    # 展示的字段
    list_display = ['id', 'name', 'floor']
    # 排序
    order_by = ['-id']
    # 搜索
    search_list = ['name', 'floor']


site.register(models.IDC, IDCConfig)

from stark.forms.forms import StarkModelForm
from stark.forms.widgets import DatePickerInput


class ServerForm(StarkModelForm):
    class Meta:
        model = models.Server
        fields = '__all__'

        widgets = {
            'latest_date': DatePickerInput(attrs={'class': 'date-picker', 'autocomplete': 'off'})
        }


class ServerConfig(StarkConfig):
    model_form_class = ServerForm

    #
    # def show_satus(self, header=None, row=None):

    # if header:
    #         return '设备状态'
    #
    #
    #     return mark_safe('<span style="color:red">{}</span>'.format(row.get_device_status_id_display()))

    def show_hostname(self, header=None, row=None):
        if header:
            return '主机名'
        return mark_safe(
            '<a href="{}"> {} </a>'.format('/stark/repository/server/server_detail/{}'.format(row.pk), row.hostname))

    def show_record(self, header=None, row=None):
        if header:
            return '变更记录'
        return mark_safe(
            '<a href="{}"> 查看 </a>'.format('/stark/repository/server/server_record/{}'.format(row.pk), ))

    # 展示的字段   可以使用内置或者自定义方法  内置get_choice_text 自定义show_hostname
    list_display = ['id', show_hostname, 'idc', 'cabinet_num', 'cabinet_order',
                    get_choice_text('device_status_id', '状态', ), show_record,
                    'latest_date']
    # 排序
    order_by = ['-id']
    # 搜索
    search_list = ['id', 'hostname', ]

    def server_detail(self, request, pk):
        obj = models.Server.objects.filter(pk=pk).first()
        disks = obj.disk_list.order_by('slot')
        return render(request, 'server_detail.html', {'obj': obj, 'disks': disks})

    def server_record(self, request, pk):
        obj = models.Server.objects.filter(pk=pk).first()
        return render(request, 'server_record.html', {'obj': obj})

    #额外补充整合详情页及变更记录
    def extra_url(self):
        urlpatterns = [

            url(r'^server_detail/(\d+)/$', self.server_detail, name='server_detail'),
            url(r'^server_record/(\d+)/$', self.server_record, name='server_record'),
        ]

        return urlpatterns

    # 组合搜索  组合筛选
    list_filter = [
        # Option('idc', is_multi=True, condition={'pk__in': [1, ]}),  # condition 只显示部分筛选条件
        Option('idc', is_multi=True, ),
        # Option('business_unit'),
        Option('device_status_id', is_choice=True, text_func=lambda x: x[1])  #choice字段额外加is_choice  无text_func则结果为元组(1,'xx')
    ]


site.register(models.Server, ServerConfig)

# site._registry = [(models.Server, ServerConfig())]
