from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from utils.verify import MatplotlibPng

from utils import constants
from .forms import SelectCellFrom, SendorForm, AlertForm

from django.db.models import Count, Max, Avg, Min, Q
from analysis.models import  PH, Base, Solid, Metal, Equip, PHAlert, SolidAlert, MetalAlert, EquipAlertRecord, AnAlert

# Create your views here.


def analysis_alert(request):
    """ 报警记录查询页面 """

    if request.method == 'POST':
        form = request.POST.get('sendor', None)
        print(form)
        cursor = connection.cursor()
        if 'p' in form:
            sql_p = "SELECT  " \
                    "p.cell, p.status , p.measure_nub, p.measure_at," \
                    " p.name_id, p.handle_no, p.handle_at, p.is_handle " \
                    "FROM ph_alert as p   "\
                    "WHERE sendor=%s "
                    # "LIMIT 10, 20"
            a = cursor.execute(sql_p, [form])
        elif 'm' in form:
            sql_m = "SELECT p.id, p.cell, p.is_status , p.measure_nub, p.measure_at  " \
                    "FROM  as p   " \
                    "WHERE sendor=%s "
                    # "LIMIT 10, 20"
            a = cursor.execute(sql_m, [form])
        elif 's' in form:
            sql_s = "SELECT p.id, p.cell, p.is_status , p.measure_nub, p.measure_at  " \
                    "FROM solid as p   " \
                    "WHERE sendor=%s "
                    # "LIMIT 10, 20"
            a = cursor.execute(sql_s, [form])
        elif 'a' in form:
            sql_s = "SELECT p.id, p.cell, p.is_status , p.measure_nub, p.measure_at  " \
                    "FROM an as p   " \
                    "WHERE sendor=%s "
                    # "LIMIT 10, 20"
            a = cursor.execute(sql_s, [form])
        else:
            analysis = []
        analysis = cursor.fetchall()
        print(analysis)
        # print(a)
    else:
        analysis = []
        form = SendorForm(request)

    return render(request, 'alert.html', {
        'form': form,
        'analysis': analysis,
    })


def analysis_history(request):
    """历史数据查询"""
    # global analysis
    if request.method == 'POST':
        form = request.POST.get('sendor', None)
        print(form)
        cursor = connection.cursor()
        if 'p' in form:
            sql_p = "SELECT p.id, p.cell, p.is_status , p.measure_nub, p.measure_at  " \
                  "FROM ph as p   " \
                  "WHERE sendor=%s "\
                  "LIMIT 10, 20"
            a = cursor.execute(sql_p, [form])
        elif 'm' in form:
            sql_m = "SELECT p.id, p.cell, p.is_status , p.measure_nub, p.measure_at  " \
                  "FROM metal as p   " \
                  "WHERE sendor=%s " \
                  "LIMIT 10, 20"
            a = cursor.execute(sql_m, [form])
        elif 's' in form:
            sql_s = "SELECT p.id, p.cell, p.is_status , p.measure_nub, p.measure_at  " \
                  "FROM solid as p   " \
                  "WHERE sendor=%s " \
                  "LIMIT 10, 20"
            a = cursor.execute(sql_s, [form])
        elif 'a' in form:
            sql_s = "SELECT p.id, p.cell, p.is_status , p.measure_nub, p.measure_at  " \
                  "FROM an as p   " \
                  "WHERE sendor=%s " \
                  "LIMIT 10, 20"
            a = cursor.execute(sql_s, [form])
        else:
            analysis = []
        analysis = cursor.fetchall()
        # print(a)
    else:
        analysis = []
        form = SendorForm(request)

    return render(request, 'history.html', {
        'form': form,
        'analysis': analysis,
    })


def index(request):
    """ 首页 """
    sql_1 = "SELECT p.measure_nub, p.is_status " \
            "FROM ph as p " \
            "WHERE p.measure_at " \
            "IN (SELECT MAX(measure_at) FROM ph as h where sendor=%s ) " \

    cursor = connection.cursor()
    ph_1_1_rest = cursor.execute(sql_1, ['ph-1-1'])
    ph_1_1 = cursor.fetchall()
    print(ph_1_1_rest)
    print(ph_1_1)
    print(sql_1)
    # sql_2 = "SELECT p.measure_nub " \
    #         "FROM ph as p " \
    #         "WHERE p.measure_at " \
    #         "IN (SELECT MAX(measure_at) FROM ph as h where sendor=%s ) "
    # ph_1_2_rest = cursor.execute(sql_2, ['ph_1_2'])
    # print(ph_1_2_rest)
    # ph_1_2 = cursor.fetchall()
    # print(ph_1_2)

    sql_3 = "SELECT p.measure_nub, p.is_status " \
            "FROM solid as p " \
            "WHERE p.measure_at " \
            "IN (SELECT MAX(measure_at) FROM solid as h group by sendor ) "
    s_rest = cursor.execute(sql_3)
    s = cursor.fetchall()
    print(s)

    sql_4 = "SELECT p.measure_nub, p.is_status " \
            "FROM an as p " \
            "WHERE p.measure_at " \
            "IN (SELECT MAX(measure_at) FROM an as h group by sendor ) "
    a_rest = cursor.execute(sql_4)
    a = cursor.fetchall()
    print(a)

    sql_5 = "SELECT p.measure_nub, p.is_status " \
            "FROM metal as p " \
            "WHERE p.measure_at " \
            "IN (SELECT MAX(measure_at) FROM metal as h group by sendor ) "
    m_rest = cursor.execute(sql_5)
    m = cursor.fetchall()
    print(m)
    rest = {
        'ph_1_1': ph_1_1,
        # 'ph_1_2': ph_1_2,
        's': s,
        'a': a,
        'm': m,
            }
    return render(request, 'index.html', rest
    )


def equip_manage(request):
    sql_1 = "SELECT p.equip_status " \
            "FROM equip as p " \
            "WHERE p.status_at " \
            "IN (SELECT MAX(status_at) FROM equip as h) "
    cursor = connection.cursor()
    rest = cursor.execute(sql_1)
    row = cursor.fetchall()
    print(row)

    return render(request, 'equip.html', {
        'row': row,
    })


def cell(request):
    sel_form = SelectCellFrom()
    return render(request, 'sel_cell.html', {
        'sel_form': sel_form
    })


def add(request):
    a = request.GET['value']
    print(a)
    a = int(a)
    return HttpResponse(str(a))


def matlp_1(request):
    sql = "SELECT p.measure_nub " \
            "FROM ph as p WHERE sendor=%s "
    cursor = connection.cursor()
    ph_1_1_rest = cursor.execute(sql, ['ph-1-1'])
    ph_1_1 = list(cursor.fetchall())
    a = MatplotlibPng(ph_1_1)
    a.draw_plt()
    return render(request, 'test.html', {
    })


def matlp_2(request):
    sql = "SELECT p.measure_nub " \
            "FROM ph as p WHERE sendor=%s "
    cursor = connection.cursor()
    ph_1_3_rest = cursor.execute(sql, ['ph-1-3'])
    ph_1_3 = list(cursor.fetchall())
    a = MatplotlibPng(ph_1_3)
    a.draw_plt()
    return render(request, 'test.html', {
    })


def matlp_3(request):
    sql = "SELECT p.measure_nub " \
            "FROM solid as p WHERE sendor=%s "
    cursor = connection.cursor()
    s_1_rest = cursor.execute(sql, ['s-1'])
    s_1 = list(cursor.fetchall())
    a = MatplotlibPng(s_1)
    a.draw_plt()
    return render(request, 'test.html', {
    })


def matlp_4(request):
    sql = "SELECT p.measure_nub " \
            "FROM solid as p WHERE sendor=%s "
    cursor = connection.cursor()
    s_3_rest = cursor.execute(sql, ['s-3'])
    s_3 = list(cursor.fetchall())
    a = MatplotlibPng(s_3)
    a.draw_plt()
    return render(request, 'test.html', {
    })


def matlp_5(request):
    sql = "SELECT p.measure_nub " \
            "FROM ph as p WHERE sendor=%s "
    cursor = connection.cursor()
    ph_2_1_rest = cursor.execute(sql, ['ph-2-1'])
    ph_2_1 = list(cursor.fetchall())
    a = MatplotlibPng(ph_2_1)
    a.draw_plt()
    return render(request, 'test.html', {
    })


def matlp_6(request):
    sql = "SELECT p.measure_nub " \
            "FROM ph as p WHERE sendor=%s "
    cursor = connection.cursor()
    ph_2_3_rest = cursor.execute(sql, ['ph-2-3'])
    ph_2_3 = list(cursor.fetchall())
    a = MatplotlibPng(ph_2_3)
    a.draw_plt()
    return render(request, 'test.html', {
    })


def matlp_7(request):
    sql = "SELECT p.measure_nub " \
            "FROM metal as p WHERE sendor=%s "
    cursor = connection.cursor()
    m_1_rest = cursor.execute(sql, ['m-1'])
    m_1 = list(cursor.fetchall())
    a = MatplotlibPng(m_1)
    a.draw_plt()
    return render(request, 'test.html', {
    })


def matlp_8(request):
    sql = "SELECT p.measure_nub " \
            "FROM metal as p WHERE sendor=%s "
    cursor = connection.cursor()
    m_2_rest = cursor.execute(sql, ['m-2'])
    m_2 = list(cursor.fetchall())
    a = MatplotlibPng(m_2)
    a.draw_plt()
    return render(request, 'test.html', {
    })


def matlp_9(request):
    sql = "SELECT p.measure_nub " \
            "FROM ph as p WHERE sendor=%s "
    cursor = connection.cursor()
    ph_3_1_rest = cursor.execute(sql, ['ph-3-1'])
    ph_3_1 = list(cursor.fetchall())
    a = MatplotlibPng(ph_3_1)
    a.draw_plt()
    return render(request, 'test.html', {
    })


def matlp_10(request):
    sql = "SELECT p.measure_nub " \
            "FROM ph as p WHERE sendor=%s "
    cursor = connection.cursor()
    ph_3_3_rest = cursor.execute(sql, ['ph-3-3'])
    ph_3_3 = list(cursor.fetchall())
    a = MatplotlibPng(ph_3_3)
    a.draw_plt()
    return render(request, 'test.html', {
    })


def matlp_11(request):
    sql = "SELECT p.measure_nub " \
            "FROM an as p WHERE sendor=%s "
    cursor = connection.cursor()
    a_1_rest = cursor.execute(sql, ['a-1'])
    a_1 = list(cursor.fetchall())
    a = MatplotlibPng(a_1)
    a.draw_plt()
    return render(request, 'test.html', {
    })


def matlp_12(request):
    sql = "SELECT p.measure_nub " \
            "FROM an as p WHERE sendor=%s "
    cursor = connection.cursor()
    a_1_rest = cursor.execute(sql, ['a-2'])
    a_1 = list(cursor.fetchall())
    a = MatplotlibPng(a_1)
    a.draw_plt()
    return render(request, 'test.html', {
    })
