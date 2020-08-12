.. _reports_quickstart:

xlwings Reports
===============

This feature requires xlwings :guilabel:`PRO`.

See also the :ref:`Reports API reference <reports_api>`.

Quickstart
----------

xlwings Reports is part of xlwings PRO and a solution for template based Excel and PDF reporting. It allows
business users without Python knowledge to create & maintain Excel templates without having
to go back to a Python developer for every change: xlwings Reports separates the Python code
(that gets and prepares all the data) from the Excel template (that defines which data goes where
and how it should be formatted). See also the `xlwings Reports homepage <https://www.xlwings.org/reporting>`_.

Start by creating the following Python script ``my_template.py``::

    from xlwings.pro.reports import create_report
    import pandas as pd

    df = pd.DataFrame(data=[[1,2],[3,4]])
    wb = create_report('my_template.xlsx', 'my_report.xlsx', title='MyTitle', df=df)

Then create the following Excel file called ``my_template.xlsx``:

.. figure:: images/mytemplate.png
    :scale: 60%

Now run the Python script::

    python my_template.py

This will copy the template and create the following output by replacing the variables in double curly braces with
the value from the Python variable:

.. figure:: images/myreport.png
    :scale: 60%

Apart from Strings and Pandas DataFrames, you can also use numbers, lists, simple dicts, NumPy arrays,
Matplotlib figures and PIL Image objects that have a filename.

By default, xlwings Reports overwrites existing values in templates if there is not enough free space for your variable.
If you want your rows to dynamically shift according to the height of your array, use :ref:`Frames`.

.. _frames:

Frames
------

Frames are vertical containers in which content is being aligned according to their height. That is,
within Frames:

* Variables do not overwrite existing cell values as they do without Frames.
* Table formatting is applied to all data rows.

To use Frames, insert ``<frame>`` into **row 1** of your Excel template wherever you want a new dyanmic column
to start. Row 1 will be removed automatically when creating the report. Frames go from one
``<frame>`` to the next ``<frame>`` or the right border of the used range.

How Frames behave is best demonstrated with an example:
The following screenshot defines two frames. The first one goes from column A to column E and the second one
goes from column F to column I.

You can define and format tables by formatting exactly

* one header and
* one data row

as shown in the screenshot:

.. figure:: images/frame_template.png
    :scale: 60%

Running the following code::

    from xlwings.pro.reports import create_report
    import pandas as pd

    df1 = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    df2 = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]])

    data = dict(df1=df1, df2=df2)

    create_report('my_template.xlsx',
                  'my_report.xlsx',
                  **data)

will generate this report:

.. figure:: images/frame_report.png
    :scale: 60%