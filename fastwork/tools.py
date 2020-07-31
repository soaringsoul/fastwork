'''
@File    :   tools.py
@Contact :   951683309@qq.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/5/14 17:26   GongliXu     1.0
'''
import os
import pandas as pd
from sqlalchemy import create_engine
import configparser


def to_excel(df, filepath, sheet_name="sheet1"):
    new_filename = "%s_处理完成.xlsx" % os.path.basename(filepath)
    abs_filepath = os.path.abspath(filepath)
    new_filepath = os.path.join(os.path.dirname(abs_filepath), new_filename)
    writer = pd.ExcelWriter('%s' % new_filepath, engine='xlsxwriter')
    df.to_excel(writer, sheet_name=sheet_name,
                startrow=0,
                index=False)
    workbook = writer.book
    # 统计部分内容部分样式
    txt_cell_format = workbook.add_format({'bold': False, 'italic': False, 'font_size': 10, 'border': 1})
    txt_cell_format.set_align('left')
    worksheet = writer.sheets['合并']
    # worksheet1.set_column(起始列,结束列，列宽，格式)
    worksheet.set_column(0, df.shape[1], 15, txt_cell_format)
    writer.save()


def mysql_engine(**kwargs):
    engine = create_engine("mysql+pymysql://%s:%s@%s/%s?charset=%s"
                           % (kwargs['user'],
                              kwargs['password'],
                              kwargs['host'],
                              kwargs['database'],
                              kwargs['charset']))
    return engine


def mssql_engine(**kwargs):
    engine = create_engine("mssql+pymssql://%s:%s@%s/%s?charset=%s"
                           % (kwargs['user'],
                              kwargs['password'],
                              kwargs['server'],
                              kwargs['database'],
                              kwargs['charset']
                              ), encoding='UTF-8')
    return engine


def read_cfg(filepath):
    db_cfg = configparser.ConfigParser()
    db_cfg.read('%s' % filepath, encoding='utf8')
    return db_cfg
