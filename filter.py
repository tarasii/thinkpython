import pandas as pd
import numpy as np
import datetime as dt
import pm
import os


class Convertor(object):
    in_file_name = ""
    out_file_name = ""
    df = None

    @classmethod
    def read(self):
        file_name, file_extension = os.path.splitext(self.in_file_name)
        if file_extension == '.xlsx':
            self.df = pd.read_excel(self.in_file_name)
        elif file_extension == '.csv':
            self.df = pd.pandas.read_csv(self.in_file_name, encoding="utf-8",  error_bad_lines=False)

    @classmethod
    def filter(self):
        pass

    @classmethod
    def write(self):
        file_name, file_extension = os.path.splitext(self.out_file_name)
        if file_extension == '.xlsx':
            writer = pd.ExcelWriter(self.out_file_name)
            self.df.to_excel(writer, 'Sheet1', index= False)
            writer.save()
        elif file_extension == '.csv':
            self.df.to_csv(self.out_file_name, encoding="utf-8", index=False)

    @classmethod
    def process(self):
        p = pm.pm()
        p.cnt("S")
        self.read()
        p.cnt("L")
        self.filter()
        p.cnt("F")
        self.write()
        p.cnt("W")



class convert_xlsx_csv(Convertor):
    in_file_name = "201711_LUD_Confidential_AXA_holdings_V0.1.xlsx"
    out_file_name = "201711_IVT_Confidential_AXA_holdings_V1.1.csv"


class filter_no_empty_isin(Convertor):
    in_file_name = "201711_IVT_Confidential_AXA_holdings_V1.1.csv"
    out_file_name = "201711_IVT_AXA_ISIN_V0.csv"

    @classmethod
    def filter(self):
        print len(self.df)
        self.df = self.df[self.df["ISIN code"].notnull()]
        print len(self.df)


class filter_empty_isin(Convertor):
    in_file_name = "201711_IVT_Confidential_AXA_holdings_V1.1.csv"
    out_file_name = "201711_IVT_AXA_NO_ISIN_V0.csv"

    @classmethod
    def filter(self):
        print len(self.df)
        self.df = self.df[~self.df["ISIN code"].notnull()]
        print len(self.df)



class filter_equties(Convertor):
    in_file_name = "201711_IVT_AXA_ISIN_V0.csv"
    out_file_name = "201711_IVT_AXA_EQUTIES_V0.csv"
    filter_list = ["Equities"] 

    @classmethod
    def filter(self):
        print len(self.df)
        #self.df = self.df[self.df["AXA holding type"] == "Equities"]
        self.df = self.df[self.df["ISIN code"].notnull()]
        self.df = self.df[self.df["AXA holding type"].isin(self.filter_list)]
        print len(self.df)


class filter_bonds(filter_equties):
    in_file_name = "201711_IVT_AXA_ISIN_V0.csv"
    out_file_name = "201711_IVT_AXA_BONDS_V0.csv"
    filter_list = ["Corporate bonds"] #["Government bonds","Corporate bonds"]


class filter_bonds_equities(filter_equties):
    #in_file_name = "AXA Data (None) V1-CONFIDENTIAL_AXA_RPT_PHY_201709.csv"
    in_file_name = "201711_IVT_Confidential_AXA_holdings_V1.1.csv"
    out_file_name = "AXA_BONDS_EQUTIES_IVT_201709.csv"
    filter_list = ["Corporate bonds", "Equities"] 


class get_statistics(Convertor):
    in_file_name = "201711_IVT_Confidential_AXA_holdings_V1.1.csv"
    out_file_name = "test.csv"

    @classmethod
    def filter(self):
        self.df["has_isin"] = self.df["ISIN code"].notnull()
        #df = self.df.groupby(['AXA holding type','has_isin'])['ISIN code'].nunique()
        #print df
        #self.df = self.df.groupby(['AXA holding type','has_isin']).size()
        self.df = self.df.groupby(['AXA holding type','has_isin'])['ISIN code'].agg(['size','nunique'])
        #self.df["unique ISIN"] = df.iloc[:,-1]

    @classmethod
    def write(self):
        print self.df

class check_bonds(Convertor):
    in_file_name = "201711_IVT_AXA_BONDS_V0.csv"
    out_file_name = "test.csv"

    @classmethod
    def filter(self):
        print len(self.df)
        #l = ["Government bonds","Corporate bonds"]
        #l = ["Corporate bonds"]
        #self.df = self.df.groupby(['ISIN code']).size()
        #self.df = self.df[self.df["AXA holding type"].isin(l)]
        self.df = self.df.groupby(['AXA holding type'])['ISIN code'].nunique()
        print len(self.df)

    @classmethod
    def write(self):
        print self.df


class check_equites(Convertor):
    in_file_name = "201711_IVT_AXA_EQUTIES_V0.csv"
    out_file_name = "test.csv"

    @classmethod
    def filter(self):
        print len(self.df)
        #l = ["Government bonds","Corporate bonds"]
        #l = ["Corporate bonds"]
        #self.df = self.df.groupby(['ISIN code']).size()
        #self.df = self.df[self.df["AXA holding type"].isin(l)]
        self.df = self.df.groupby(['AXA holding type'])['ISIN code'].nunique()
        print len(self.df)

    @classmethod
    def write(self):
        print self.df

class isin_statistics(Convertor):
    in_file_name = "AXA_BONDS_EQUTIES_IVT_201709.csv"
    out_file_name = "201711_IVT_AXA_EQUTIES_V0.csv"
    filter_list = ["Equities"]

    @classmethod
    def filter(self):
        print len(self.df)
        # self.df = self.df[self.df["AXA holding type"] == "Equities"]
        self.df = self.df["ISIN code"].value_counts()
        print len(self.df)

    @classmethod
    def write(self):
        print self.df


class isin_filter(Convertor):
    in_file_name = "AXA_BONDS_EQUTIES_IVT_201709.csv"
    out_file_name = "AXA_XS1642502295_IVT_201711.xlsx"
    filter_list = ["XS1680848030"]

    @classmethod
    def filter(self):
        print len(self.df)
        # self.df = self.df[self.df["ISIN code"] == "XS1642502295"]
        self.df = self.df[self.df["ISIN code"].isin(self.filter_list)]
        print len(self.df)


class filter_government_bonds(filter_equties):
    #in_file_name = "AXA Data (None) V1-CONFIDENTIAL_AXA_RPT_PHY_201709.csv"
    in_file_name = "201711_IVT_Confidential_AXA_holdings_V1.1.csv"
    out_file_name = "AXA_BONDS_GOVERNMENT_BONDS_IVT_201801.xlsx"
    filter_list = ["Government bonds",] 
    @classmethod
    def filter(self):
        super(filter_government_bonds, self).filter()
        #print self.df.columns.values 
        self.df = self.df[['Issuer long name','Local code','Issuer nationality','Issue Date','Maturity','Dividend/Coupon','AXA External Issuer rating','AXA Internal Issuer rating','AXA External Rating','Ultimate Shareholder Rating','AXA external Counterparty of support rating','Issuer Second Best Rating','Security Second Best Rating']]
        self.df = self.df.drop_duplicates()
        print len(self.df)

class filter_government_related(filter_equties):
    #in_file_name = "AXA Data (None) V1-CONFIDENTIAL_AXA_RPT_PHY_201709.csv"
    in_file_name = "201711_IVT_Confidential_AXA_holdings_V1.1.csv"
    out_file_name = "AXA_BONDS_GOVERNMENT_RELATED_IVT_201801.xlsx"
    filter_list = ["Government related",] 

    @classmethod
    def filter(self):
        super(filter_government_related, self).filter()
        #print self.df.columns.values 
        self.df = self.df[['Issuer long name','Local code','Issuer nationality','Issue Date','Maturity','Dividend/Coupon','AXA External Issuer rating','AXA Internal Issuer rating','AXA External Rating','Ultimate Shareholder Rating','AXA external Counterparty of support rating','Issuer Second Best Rating','Security Second Best Rating']]
        self.df = self.df.drop_duplicates()
        print len(self.df)

#filter_no_empty_isin.process()
#filter_equties.process()
#filter_bonds.process()

#get_statistics.process()
#check_bonds.process()
#check_equites.process()
#filter_bonds_equities.process()
#isin_statistics.process()
#isin_filter.process()
filter_government_bonds.process()
filter_government_related.process()
