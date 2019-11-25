from django import forms
from acc.models import All_Device
from .models import *


class cant_test_Form(forms.ModelForm):
    class Meta:
        model = cant_test
        #fields = '__all__'
        exclude = ['record', 'user', 'date', 'is_done']


class monitor_spO2_1_Form(forms.ModelForm):
    class Meta:
        model = monitor_spo2_1
        #fields = '__all__'
        exclude = ['is_done', 'is_recal', 'ref_record', 'record', 'user', 'date', 'licence',
                   'cal_dev_1_cd', 'cal_dev_1_xd', 'cal_dev_2_cd', 'cal_dev_2_xd', 'cal_dev_3_cd', 'cal_dev_3_xd']


class monitor_ecg_1_Form(forms.ModelForm):
    class Meta:
        model = monitor_ecg_1
        #fields = '__all__'
        exclude = ['is_done', 'is_recal', 'ref_record', 'record', 'user', 'date', 'licence',
                   'cal_dev_1_cd', 'cal_dev_1_xd', 'cal_dev_2_cd', 'cal_dev_2_xd', 'cal_dev_3_cd', 'cal_dev_3_xd']


class monitor_nibp_1_Form(forms.ModelForm):
    class Meta:
        model = monitor_nibp_1
        #fields = '__all__'
        exclude = ['is_done', 'is_recal', 'ref_record', 'record', 'user', 'date', 'licence',
                   'cal_dev_1_cd', 'cal_dev_1_xd', 'cal_dev_2_cd', 'cal_dev_2_xd', 'cal_dev_3_cd', 'cal_dev_3_xd']


class aed_1_Form(forms.ModelForm):
    class Meta:
        model = aed_1
        #fields = '__all__'
        exclude = ['is_done', 'is_recal', 'ref_record', 'record', 'user', 'date',
                   'licence', 'cal_dev_1_cd', 'cal_dev_1_xd', 'cal_dev_2_cd', 'cal_dev_2_xd']


class monitor_safety_1_Form(forms.ModelForm):
    class Meta:
        model = monitor_safety_1
        #fields = '__all__'
        exclude = ['is_done', 'is_recal', 'ref_record', 'record', 'user', 'date', 'licence', 'cal_dev_1_cd',
                   'cal_dev_1_xd', 'cal_dev_2_cd', 'cal_dev_2_xd', 'cal_dev_3_cd', 'cal_dev_3_xd']


class anesthesia_machine_1_Form(forms.ModelForm):
    class Meta:
        model = anesthesia_machine_1
        #fields = '__all__'
        exclude = ['is_done', 'is_recal', 'ref_record', 'record', 'user', 'date', 'licence', 'cal_dev_1_cd',
                   'cal_dev_1_xd', 'cal_dev_2_cd', 'cal_dev_2_xd', 'cal_dev_3_cd', 'cal_dev_3_xd', 'cal_dev_4_cd', 'cal_dev_4_xd']


class defibrilator_1_Form(forms.ModelForm):
    class Meta:
        model = defibrilator_1
        #fields = '__all__'
        exclude = ['is_done', 'is_recal', 'ref_record', 'record', 'user', 'date', 'licence', 'cal_dev_1_cd',
                   'cal_dev_1_xd', 'cal_dev_2_cd', 'cal_dev_2_xd', 'cal_dev_3_cd', 'cal_dev_3_xd', 'cal_dev_4_cd', 'cal_dev_4_xd']


class ecg_1_Form(forms.ModelForm):
    class Meta:
        model = ecg_1
        #fields = '__all__'
        exclude = ['is_done', 'is_recal', 'ref_record', 'record', 'user', 'date', 'licence', 'cal_dev_1_cd',
                   'cal_dev_1_xd', 'cal_dev_2_cd', 'cal_dev_2_xd', 'cal_dev_3_cd', 'cal_dev_3_xd', 'cal_dev_4_cd', 'cal_dev_4_xd']


class flowmeter_1_Form(forms.ModelForm):
    class Meta:
        model = flowmeter_1
        #fields = '__all__'
        exclude = ['is_done', 'is_recal', 'ref_record', 'record',
                   'user', 'date', 'licence', 'cal_dev_1_cd', 'cal_dev_1_xd']


class infusion_pump_1_Form(forms.ModelForm):
    class Meta:
        model = infusion_pump_1
        #fields = '__all__'
        exclude = ['is_done', 'is_recal', 'ref_record', 'record', 'user', 'date', 'licence', 'cal_dev_1_cd',
                   'cal_dev_1_xd', 'cal_dev_2_cd', 'cal_dev_2_xd', 'cal_dev_3_cd', 'cal_dev_3_xd', 'cal_dev_4_cd', 'cal_dev_4_xd']


class monometer_1_Form(forms.ModelForm):
    class Meta:
        model = monometer_1
        #fields = '__all__'
        exclude = ['is_done', 'is_recal', 'ref_record', 'record', 'user', 'date', 'licence',
                   'cal_dev_1_cd', 'cal_dev_1_xd', 'cal_dev_2_cd', 'cal_dev_2_xd', 'cal_dev_3_cd', 'cal_dev_3_xd']


class spo2_1_Form(forms.ModelForm):
    class Meta:
        model = spo2_1
        #fields = '__all__'
        exclude = ['is_done', 'is_recal', 'ref_record', 'record', 'user', 'date', 'licence', 'cal_dev_1_cd',
                   'cal_dev_1_xd', 'cal_dev_2_cd', 'cal_dev_2_xd', 'cal_dev_3_cd', 'cal_dev_3_xd', 'cal_dev_4_cd', 'cal_dev_4_xd']


class suction_1_Form(forms.ModelForm):
    class Meta:
        model = suction_1
        #fields = '__all__'
        exclude = ['is_done', 'is_recal', 'ref_record', 'record', 'user', 'date', 'licence', 'cal_dev_1_cd',
                   'cal_dev_1_xd', 'cal_dev_2_cd', 'cal_dev_2_xd', 'cal_dev_3_cd', 'cal_dev_3_xd', 'cal_dev_4_cd', 'cal_dev_4_xd']


class syringe_pump_1_Form(forms.ModelForm):
    class Meta:
        model = syringe_pump_1
        #fields = '__all__'
        exclude = ['is_done', 'is_recal', 'ref_record', 'record', 'user', 'date', 'licence', 'cal_dev_1_cd',
                   'cal_dev_1_xd', 'cal_dev_2_cd', 'cal_dev_2_xd', 'cal_dev_3_cd', 'cal_dev_3_xd', 'cal_dev_4_cd', 'cal_dev_4_xd']


class electrocauter_1_Form(forms.ModelForm):
    class Meta:
        model = electrocauter_1
        #fields = '__all__'
        exclude = ['is_done', 'is_recal', 'ref_record', 'record', 'user', 'date', 'licence', 'cal_dev_1_cd', 'cal_dev_1_xd',
                   'cal_dev_2_cd', 'cal_dev_2_xd', 'cal_dev_3_cd', 'cal_dev_3_xd', 'cal_dev_4_cd', 'cal_dev_4_xd', 'cal_dev_5_cd', 'cal_dev_5_xd']


class ventilator_1_Form(forms.ModelForm):
    class Meta:
        model = ventilator_1
        #fields = '__all__'
        exclude = ['is_done', 'is_recal', 'ref_record', 'record', 'user', 'date', 'licence', 'cal_dev_1_cd',
                   'cal_dev_1_xd', 'cal_dev_2_cd', 'cal_dev_2_xd', 'cal_dev_3_cd', 'cal_dev_3_xd', 'cal_dev_4_cd', 'cal_dev_4_xd']
