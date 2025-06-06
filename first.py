import streamlit as st
import pandas as pd

st.set_page_config(page_title='🍉南宁美食地图')

df = pd.DataFrame({
    "latitude":[22.833240,22.849230,22.814151,22.818193,22.830622],
    "longitude":[108.403855,108.320469,108.321510,108.292848,108.371383]})
df.index.name='序号'
st.map(df)

data = {
    '餐厅名称': ['复记老友粉', '好友缘', '星艺会尝不忘', '白妈螺蛳粉', '高峰柠檬鸭'],
    "类型": ["早餐", "中餐", "快餐", "自助餐", "西餐"],
    '评分': [4, 4.8, 4.2, 4.3, 4.4],
     "人均消费(元)": [15, 20, 25, 35, 50],
    '时段':[11,11.5,12,12.5,13],
     '复记老友粉':[200, 150, 180,150,160],
    '星艺会尝不忘':[120, 160, 123,180,130],
    '高峰柠檬鸭':[110, 100, 160,150,170],
}

df=pd.DataFrame(data)
st.header('⭐️餐厅评分')
st.bar_chart(df,y='评分',x='餐厅名称')
df.set_index=('name')

st.header('🔔不同类型餐厅价格')
st.line_chart(df,y='人均消费(元)',x='类型')

st.subheader("⏰用餐高峰时段")
st.area_chart(df, y=['星艺会尝不忘','高峰柠檬鸭','复记老友粉'])


st.header("🍽餐厅详情")
selected_restaurant = st.selectbox("选择餐厅查看详情", df["餐厅名称"])
selected_df = df[df["餐厅名称"] == selected_restaurant]
st.subheader(f"评分：{selected_df.iloc[0]['评分']}/5.0")
st.subheader(f"人均消费(元)：{selected_df.iloc[0]['人均消费(元)']}元")
st.write("推荐菜品:特色套餐,地方小吃,时令蔬菜")

st.header("当前拥挤程度")
st.markdown('###### 94%拥挤')
st.progress(94)
st.title("🎲今日午餐推荐")
if st.button('帮我选午餐'):
    st.write('`*星艺会尝不忘*`')
    st.image("https://tse2-mm.cn.bing.net/th/id/OIP-C.i982znXoIr1SAPGvh_VfVwHaFd?w=239&h=180&c=7&r=0&o=5&pid=1.7")