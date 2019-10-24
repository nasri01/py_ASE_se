import io, pytz, xlsxwriter, jdatetime
from jdatetime import timedelta

from form.models import *
from acc.models import excel_arg ,aUserProfile as uu

from django.contrib.staticfiles.templatetags.staticfiles import static
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string


from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration


model_list = [monitor_spo2_1]


def xlsx(request):
    if request.method =='GET':

        ey, em, ed = request.GET['end_date'].split('/')
        sy, sm, sd = request.GET['start_date'].split('/')
        ey = int(ey)
        em = int(em)
        ed = int(ed)
        sy = int(sy)
        sm = int(sm)
        sd = int(sd)
        new_start_date = jdatetime.date(sy, sm, sd)-timedelta(days=1)
        #because quering from data base we should consider filter data via utc time
        start = jdatetime.datetime(new_start_date.year, new_start_date.month, new_start_date.day, 19, 30).astimezone(pytz.timezone('UTC'))
        end = jdatetime.datetime(ey, em, ed, 19, 30).astimezone(pytz.timezone('UTC'))
        if(end < start):
            if (jdatetime.date.today().month < 10):
                mm = f'0{jdatetime.date.today().month}'
            else:
                mm = jdatetime.date.today().month
            return render(request, 'acc/hospital/index.html', {'date_error': 'بازه زمانی وارد شده نا معتبر است', 'flag': 1, 'date': jdatetime.date.today(), 'month': mm})


        ##Create Excel
        data = []
        try:
            if (request.GET['is_recal'] == 'on'):
                for model in model_list:
                    modelobj = model.objects.filter(date__gte=start).filter(date__lte=end).filter(
                        request__hospital__user__id__exact=request.user.id).filter(is_recal=True)
                    data.extend(modelobj)
        except:
                for model in model_list:
                    modelobj = model.objects.filter(date__gte=start).filter(date__lte=end).filter(
                        request__hospital__user__id__exact=request.user.id)
                    data.extend(modelobj)
        


        fr1 = excel_arg.objects.all().order_by('order')
        if (request.GET['action'] == 'download'):

            output = io.BytesIO()
            wb = xlsxwriter.Workbook(output)
            ws = wb.add_worksheet()
            ws.right_to_left()
            ws.set_default_row(height=40)
            ws.set_column(0, 15, 17)

            ##first row
            first_row = (str(fr1[1]),
                         str(fr1[2]),
                         str(fr1[3]),
                         str(fr1[4]),
                         str(fr1[5]),
                         str(fr1[6]),
                         str(fr1[7]),
                         str(fr1[8]),
                         str(fr1[9]),
                         str(fr1[10]),
                         str(fr1[11]),
                         str(fr1[12]),
                         str(fr1[13]),
                         str(fr1[14]),
                         str(fr1[15])
                         )
            fr = wb.add_format({'font_size': 11, 'align': 'center', 'valign': 'vcenter', 'bottom': True,'left': True})

            ws.write_row(row= 0, col= 0 , data=first_row , cell_format=fr)
            #Patterns
            gg = wb.add_format(#accept
                {'font_size': 11, 'align': 'center', 'valign': 'vcenter', 'pattern': 1, 'bg_color': 'green', 'bottom': True,
                 'left': True})
            yy = wb.add_format(#conditional
                {'font_size': 11, 'align': 'center', 'valign': 'vcenter', 'pattern': 1, 'bg_color': 'yellow', 'bottom': True,
                 'left': True})
            rr = wb.add_format(#reject
                {'font_size': 11, 'align': 'center', 'valign': 'vcenter', 'pattern': 1, 'bg_color': 'red', 'bottom': True,
                 'left': True})
            cursor = 1


            for idata in data:
                #if (modelobj[i].device.hospital.user == request.user):
                # Assign Status
                if (idata.status.id == 1):  # accept
                    fstate = gg
                elif (idata.status.id == 2):  # conditional
                    fstate = yy
                elif (idata.status.id == 3):  # conditional
                    fstate = rr
                else:
                    fstate = fr
                total_com = ''
                for t in idata.totalcomment.all():
                    total_com += f'{t}-'


                data = (cursor,
                        idata.device.hospital.city.state_name.name,
                        idata.device.hospital.city.name,
                        idata.device.hospital.name,
                        idata.device.section.name,
                        idata.device.name.type.name,
                        idata.device.name.creator.name,
                        idata.device.name.name,
                        idata.device.serial_number,
                        idata.device.property_number,
                        idata.status.status,
                        str(idata.date.astimezone(pytz.timezone('Asia/Tehran'))).split()[0],
                        str(fr1[0]),
                        idata.licence.number,
                        total_com
                        )

                ws.write_row(row=cursor, col=0, data=data, cell_format=fstate)
                cursor += 1
            wb.close()

            output.seek(0)
            filename = f'Azma_Saba.ExcelReport.{str(jdatetime.date.today()).split()[0]}.xlsx'
            response = HttpResponse(output,content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename=%s' % filename

            return response


        else:#display table


            if (jdatetime.date.today().month < 10):
                mm = f'0{jdatetime.date.today().month}'
            else:
                mm = jdatetime.date.today().month

            return render(request, 'acc/hospital/index.html', {'firstrow':fr1,'data':data,'date':jdatetime.date.today(),'month': mm})

    #return render(request, 'acc/hospital/index.html', { 'status': 'Successfully Created!','hflag':1})
        #return FileResponse(wb,as_attachment=True,filename=f'report {datetime.date.today()}.xlsx')




def pdf(request):
    t = monitor_spo2_1.objects.get(pk=1)
    t2 = jdatetime.datetime.today()

    return render(request, 'report/Monitor/Spo2/licence1/cover.html', {'spo2': t, 'day': t2})



def pdf1(request):
    if request.method == 'GET':



#        for model in fulmodellist:
        modelobj = anesthesia_machine_1.objects.filter(licence__number=2011)
  #          if(len(modelobj) == 1):
   #             break


            #TODO licence doesn't exist

        t2 = jdatetime.datetime.today()

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = (
            'inline; '
            'filename=letter.pdf'
        )
        COMPONENTS = [
            'report/anesthesiamachine/licence1.html',
            # 'report/Defiblliators/licence1/page1.html',
            # 'report/Defiblliators/licence1/page2.html',
            # 'report/Defiblliators/licence1/page3.html',
            # 'report/Defiblliators/licence1/page4.html',
            # 'report/Defiblliators/licence1/page5.html',
            # 'report/Defiblliators/licence1/page6.html',
            # 'report/Defiblliators/licence1/page7.html',

        ]
        documents = []
        font_config = FontConfiguration()
        for template_name in COMPONENTS:
            html = render_to_string(template_name, {
                'form': modelobj[0],'time':t2 ,
            })

            css_root = static('/css')


            css1 = CSS(filename=f'ww/{css_root}/sop2-pdf.css')
            css2 = CSS(filename=f'ww/{css_root}/bootstrap-v4.min.css')


            document = HTML(string=html).render(font_config=font_config,stylesheets=[css1,css2])
            documents.append(document)

        all_pages = [page for document in documents for page in document.pages]
        documents[0].copy(all_pages).write_pdf(response)

        return response


