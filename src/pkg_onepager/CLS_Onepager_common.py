#import datetime as dt
#import numpy as np
import io
import base64    

import matplotlib.pyplot as plt
from matplotlib.dates import MonthLocator, DateFormatter
from email.mime.image import MIMEImage

import pkg_onepager.config_module as config_onepager
import pkg_common.utils as ut



class CLS_Onepager_common():
    
    def __init__(self):
        #print("Class report initiated.")
        pass
        
    def generate_html_header(self, message_title):
        content_HTML = '''
                        <html>
                            <head>
                                <style>
                                    body                    {background-color: #FFFFFF;}
                                    hr                      {margin-left: auto; margin-right: auto; margin-top: 0.01em; margin-bottom: 0.01em; background-color: #777;  height: 1px;}
                                    .style_title            {font: bold 16px Verdana, Geneva, sans-serif; display: inline-block;}
                                    .style_table            {border: 0px; padding: 1px; border-spacing: 0px; }
                                    .style_table2           {border: 1px dotted; border-color:#8A8789;  padding: 0px; border-spacing: 0px;  border-collapse: collapse;}
                                    .style_table_header     {border: 0px; background-color:#95B5DD; width: 200px; text-align: left;   font: bold 14px Verdana, Geneva, sans-serif;}
                                    .style_table_header2    {border: 0px; background-color:#95B5DD; width: 150px; text-align: center; font: bold 14px Verdana, Geneva, sans-serif;}
                                    .style_table_header3    {border: 0px; background-color:#95B5DD; width: 60px;  text-align: center; font: bold 14px Verdana, Geneva, sans-serif;}
                                    .style_table_header4    {border: 0px; background-color:#95B5DD; width: 100px; text-align: center; font: bold 14px Verdana, Geneva, sans-serif;}
                                    .style_table_header5    {border: 0px; background-color:#95B5DD; width: 100px; text-align: center; font: bold 13px Verdana, Geneva, sans-serif;}
                                    .style_table_row        {background-color:#CDD6DB;}
                                    .style_content_left     {text-align: left; width: 500px; padding-top: 0px; vertical-align: top;}
                                    .style_column_space     {width:  10px;}
                                    .style_content_right    {text-align: right; width: 580px; padding-top: 0px; vertical-align: top;}
                                    .style_table_content    {text-align: left;  width: 200px;  font: normal 14px Verdana, Geneva, sans-serif;}
                                    .style_table_content2   {text-align: right; width: 90px;  font: normal 14px Verdana, Geneva, sans-serif;}
                                    .style_table_content3   {text-align: right; width:  35px;  font: normal 14px Verdana, Geneva, sans-serif;}
                                    .style_table_content4   {text-align: right; width:  25px;  font: normal 14px Verdana, Geneva, sans-serif;}
                                    .style_table_content5   {text-align: center; width: 60px;  font: normal 14px Verdana, Geneva, sans-serif;}
                                    .style_table_content6   {text-align: center; width: 125px; font: normal 14px Verdana, Geneva, sans-serif;}
                                    .style_table_content7   {text-align: left; font: normal 10px Verdana, Geneva, sans-serif;}
                                </style>
                            </head>
                        '''
            
        content_HTML += f'''
                            <body>
                                <table>
                                    <tr>
                                        <td>
                                            <font color='red'><b><i>(This report is on validation phase)</i></b></font>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>
                                            <h2 class='text-align: left;'>{message_title}</h2>
                                        </td>
                                    </tr>
                                </table>
                                
                    '''

        #content_HTML = content_HTML.replace("                            ","")
        return content_HTML

    
    def generate_html_footer(self):
        content_HTML = '''
                                <p><i>SRM Analytics | In case of inquiries, please click <a href = "mailto:rubensh@iadb.org?subject = SRM Markets Monitor feedback">here</a>.</i></p>
                            </body>
                        </html>
                    '''
        #content_HTML = content_HTML.replace("                            ","")
        return content_HTML
    
    
    
    
    
        #Code for plotly not being used
        
        # import plotly.graph_objects as go
        # from plotly.graph_objects import Layout
        # import plotly
        
        #period_start_dt = ut.find_previous_quarter_date(config_onepager.last_12m_dt)
        
        # plotly chart 
        # ########################################################
        # layout = Layout(plot_bgcolor='rgba(0,0,0,0)', margin=dict(l=20, r=20, t=40, b=10), width=500, height=380, title=f'{ticker_query}')
        # fig = go.Figure([go.Scatter(x=df_historic.index, y=df_historic[ticker_query])], layout=layout)
        # fig.update_xaxes(showline=True, linewidth=1, linecolor='black',showgrid = True, gridwidth = 1, gridcolor='#F3F0EF', nticks=6, range=[period_start_dt,period_end_dt+ dt.timedelta(days=30)])
        # fig.update_yaxes(showline=True, linewidth=1, linecolor='black',showgrid = True, gridwidth = 1, gridcolor='#F3F0EF')
        
        # # the following line creates an interactive chart in HTML. Unfortunately does not work in emails.
        # #content_HTML += plotly.io.to_html(fig)

        # ticker_img_name = "img_" + ticker_query.replace(" ", "")
        # img = MIMEImage(fig.to_image(format="png",width=600, height=350))
        # img.add_header('Content-Disposition', 'attachment', filename=ticker_img_name)
        # img.add_header('X-Attachment-Id', ticker_img_name)
        # img.add_header('Content-ID', f'<{ticker_img_name}>')
        # message.message.attach(img)
        # ########################################################
