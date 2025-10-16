import streamlit as st
import pandas as pd
import numpy_financial as npf
from your_module import real_estate_sym_base  # クラス定義を別ファイルにしておく

st.title("不動産キャッシュフローシミュレーター")

# 📥 ユーザー入力フォーム
price = st.number_input("物件価格（万円）", value=6200)
closing_costs = st.number_input("初期費用（万円）", value=200)
term = st.number_input("返済期間（年）", value=35)
rate_year = st.number_input("年利（例：0.006）", value=0.006)
management_fee_month = st.number_input("月額管理費（万円）", value=1.2)
repair_fund_month = st.number_input("月額修繕積立金（万円）", value=1.0)
inflation = st.number_input("インフレ率（例：0.02）", value=0.02)
square_meters = st.number_input("面積（㎡）", value=70)
building_ratio = st.number_input("建屋比率", value=0.33)
site_ratio = st.number_input("土地比率", value=0.66)

# 🚀 実行ボタン
if st.button("シミュレーション実行"):
    sim = real_estate_sym_base(
        price, closing_costs, term, rate_year,
        management_fee_month, repair_fund_month, inflation,
        square_meters, building_ratio, site_ratio
    )

    df = pd.DataFrame(sim.payment_amount,
                      columns=["年目", "元本", "元本返済額", "金利返済額", "管理費", "修繕費", "固定資産税(建物)", "固定資産税(土地)", "トータル支払額"])

    st.subheader("年次キャッシュフロー")
    st.dataframe(df)

    st.line_chart(df[["元本返済額", "金利返済額", "管理費", "修繕費", "トータル支払額"]])