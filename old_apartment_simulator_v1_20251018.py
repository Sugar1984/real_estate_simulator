import numpy_financial as npf
import pandas as pd

class real_estate_sym_base:
    def __init__(self, price, closing_costs, term, rate_year, management_fee_month, repair_fund_month, inflation, square_meters, building_ratio, site_ratio):
        rate = rate_year
        nper = term
        pv = (price + closing_costs) * 10000
        fv = 0
        when = "end"

        self.payment_amount = []
        self.columns_name = ["年目", "元本", "元本返済額", "金利返済額", "管理費", "修繕費", "固定資産税(建物)", "固定資産税(土地)", "トータル支払額"]
        principal = pv

        for i in range(1, term + 1):
            principal_payment = -npf.ppmt(rate/100, i, nper, pv, fv=fv, when=when)
            interest_payment = -npf.ipmt(rate/100, i, nper, pv, fv=fv, when=when)
            management_fee = management_fee_month * 12 * (1 + inflation/100) ** (i - 1) * 10000
            repair_fund = repair_fund_month * 12 * (1 + inflation/100) ** (i - 1) * 10000
            principal -= principal_payment

            bulding_tax = price * building_ratio/100 * 0.014 * (48 - i) / 47 * 10000
            site_tax = (price * 0.7) * (1 / 6) * 0.014 * 10000
            total_payment = principal_payment + interest_payment + management_fee + repair_fund + bulding_tax + site_tax

            self.payment_amount.append([
                i,
                int(principal),
                int(principal_payment),
                int(interest_payment),
                int(management_fee),
                int(repair_fund),
                int(bulding_tax),
                int(site_tax),
                int(total_payment)
            ])

    def to_dataframe(self):
        return pd.DataFrame(self.payment_amount, columns=self.columns_name)