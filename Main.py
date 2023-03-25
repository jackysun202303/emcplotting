from pyecharts.globals import ThemeType
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
from pyecharts import options as opts
from pyecharts.charts import Bar, Line



def line(df, add_selectbox_y, add_selectbox_y_extend_1,add_selectbox_y_extend_2,add_selectbox_y_extend_3, add_selectbox_x):
    df['index'] = df.index
    # 在坐标轴中添加鼠标互动参考线
    tooltip_opts = opts.TooltipOpts(is_show=True, trigger_on="mousemove | click", axis_pointer_type='cross')

    if len(add_selectbox_x) == 0:
        axis_x = df['index'].tolist()
    else:
        axis_x = add_selectbox_x

    line = Line(init_opts=opts.InitOpts(width="2000px", height="600px"))
    line.add_xaxis(df['index'].tolist())

    # 在右侧添加y轴
    line.extend_axis(yaxis=opts.AxisOpts(type_="value", position="right", ))
    for i in add_selectbox_y:
        line.add_yaxis(i, df[i].values.tolist(),
                       markpoint_opts=opts.MarkPointOpts(
                           data=[opts.MarkPointItem(type_="max", name="最大值"),
                                 opts.MarkPointItem(type_="min", name="最小值")]))
    # 设置将销量和收益设置为右侧y轴
    line.extend_axis(yaxis=opts.AxisOpts(type_="value", position="right", offset=40 ))
    for i in add_selectbox_y_extend_1:
        line.add_yaxis(i, df[i].values.tolist(), yaxis_index=1,
                       markpoint_opts=opts.MarkPointOpts(
                            data=[opts.MarkPointItem(type_="max", name="最大值"),
                                opts.MarkPointItem(type_="min", name="最小值")]))

    line.extend_axis(yaxis=opts.AxisOpts(type_="value", position="right", offset=80))
    for i in add_selectbox_y_extend_2:
        line.add_yaxis(i, df[i].values.tolist(), yaxis_index=2,
                       markpoint_opts=opts.MarkPointOpts(
                            data=[opts.MarkPointItem(type_="max", name="最大值"),
                                opts.MarkPointItem(type_="min", name="最小值")]))

    line.extend_axis(yaxis=opts.AxisOpts(type_="value", position="right", offset=120))
    for i in add_selectbox_y_extend_3:
        line.add_yaxis(i, df[i].values.tolist(), yaxis_index=2,
                       markpoint_opts=opts.MarkPointOpts(
                            data=[opts.MarkPointItem(type_="max", name="最大值"),
                                opts.MarkPointItem(type_="min", name="最小值")]))


    line.set_global_opts(title_opts=opts.TitleOpts(title="译码数据", pos_left="middle", pos_top="top"),
                         legend_opts=opts.LegendOpts(type_="scroll", pos_left="70%", orient="horizontal"),
                         tooltip_opts=tooltip_opts,  # 在坐标轴中添加鼠标互动参考线
                         # datazoom_opts=opts.DataZoomOpts(is_show=True,orient='vertical'),
                         datazoom_opts=opts.DataZoomOpts(is_show=True, orient='horizontal'),
                         toolbox_opts=opts.ToolboxOpts(orient='vertical', pos_left='93%'),  # 增加工具栏
                         )

    line.render(r'C:\Plotting.html')
    line.render_notebook()
    line2Html = line.render_embed()
    components.html(line2Html, height=900, width=2000,scrolling=True)


# 侧边栏
graph_color = st.sidebar.color_picker('设置颜色:')
upload_file = st.sidebar.file_uploader(label="上传excel文件")

if upload_file is not None:
    # 不为空
    df = pd.read_csv(upload_file, encoding='ISO-8859-1')
    st.success("上传文件成功！")
    select_list = df.columns.values.tolist()
    add_selectbox_y = st.sidebar.multiselect("选择Y_1轴相应的参数（可多选）：", (select_list))
    add_selectbox_y_extend_1 = st.sidebar.multiselect("选择Y_2轴次坐标（可多选）：", (select_list))
    add_selectbox_y_extend_2 = st.sidebar.multiselect("选择Y_3轴次坐标（可多选）：", (select_list))
    add_selectbox_y_extend_3 = st.sidebar.multiselect("选择Y_4轴次坐标（可多选）：", (select_list))
    add_selectbox_x = st.sidebar.selectbox("选择X轴相应的参数（单选）：", (select_list))
    line(df, add_selectbox_y, add_selectbox_y_extend_1,add_selectbox_y_extend_2,add_selectbox_y_extend_3, add_selectbox_x)


else:
    st.warning("请上传文件！")  # 退出




