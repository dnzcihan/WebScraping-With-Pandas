import pandas as  pd
from bs4 import BeautifulSoup
import urllib3
http = urllib3.PoolManager()
url = "https://liderform.com.tr/program/performance"
response = http.request('GET', url)
soup = BeautifulSoup(response.data,'lxml')
city = []
for table in soup.findAll('div',attrs={'class':"tabs-content-block"}):
    for td in table.findAll('ul',attrs={'class':'secondary-header wrap'}):
        for a in td.findAll('a',attrs={'class':None}):
            city.append(a['href'])
sehir1=str(city[0])
sehir2=str(city[1])
sehir2
dfff = pd.read_html(sehir1)
dfff
def program():
    
    dff=pd.read_html(sehir1)
    saatler = []
    
    for table in soup.findAll('div', attrs={'class': 'race-block__time'}):
        for td in table.findAll('ul', attrs={'class': None}):
            for a in td.findAll('a', attrs={'class': None}):
                    saatler.append(a['href'])
    for b in range(0, len(saatler)):
        df = pd.read_html(saatler[b])
        tarih=[]
        for table in soup.findAll('table', attrs={'class': 'table-format-normal perfomance-border perfomance-table-style'}):
            for td in table.findAll('td', attrs={'class':None}):
                for a in td.findAll('a', attrs={'class': None}):
                    tarih.append(a['href'])
            ss=[]
        for t in range(0,len(tarih)):
            df3=pd.read_html(tarih[t])
            if len(df3[0].values[0])<8:
                continue
            
            o=list(df3[0]['H.P'].values)
                #o.sort()
            ss.append(o)
                   

        deneme = []
        for j in range(0,len(df)):
                    
            
            for k in range(1, len(df[j])):
                   
                       
                    if j%2==0:
                        continue
                    
                    if len(df[j].values[0])<8:
                         continue
                    
                    if j==1:
                        d=({'Tarih': df[j].values[k][0:][0], 'Sehir': df[j].values[k][1:][0],
                                'Şart:': df[j].values[k][2:][0], 'Pist': df[j].values[k][3:][0],
                                'PD': df[j].values[k][4:][0], 'KG': df[j].values[k][5:][0],
                                'Jokey': df[j].values[k][6:][0], 'SN': df[j].values[k][7:][0],
                                'S/K': df[j].values[k][8:][0], 'Derece': df[j].values[k][9:][0],
                                'Takı': df[j].values[k][10:][0], 'D/800': df[j].values[k][11:][0],
                                'Tabela & B. Farkları': df[j].values[k][12:][0], 'AGF': df[j].values[k][13:][0],
                                'H.P': df[j].values[k][14:][0], 'İkr': df[j].values[k][15:][0],'yarış saati':b,'Tablo':j})
                        
                        
                    d=({'Tarih': df[j].values[k][1:][0], 'Sehir': df[j].values[k][2:][0],
                            'Şart:': df[j].values[k][3:][0], 'Pist': df[j].values[k][4:][0],
                            'PD': df[j].values[k][5:][0], 'KG': df[j].values[k][6:][0],
                            'Jokey': df[j].values[k][7:][0], 'SN': df[j].values[k][8:][0],
                            'S/K': df[j].values[k][9:][0], 'Derece': df[j].values[k][10:][0],
                            'Takı': df[j].values[k][11:][0], 'D/800': df[j].values[k][12:][0],
                            'Tabela & B. Farkları': df[j].values[k][13:][0], 'AGF': df[j].values[k][14:][0],
                            'H.P': df[j].values[k][15:][0], 'İkr': df[j].values[k][16:][0],'yarış saati':b ,'Tablo':j,'H.P Puanları':ss[k-1]})
           
                    deneme.append(d)
    
        deneme = pd.DataFrame(deneme)
        ad = 'şehir1 yaris{0}.xlsx'.format(b)
        ad = str(ad)
        writer = pd.ExcelWriter(ad)
        deneme.to_excel(writer,'Sheet{0}')  
        writer.save()




def program2():
    http = urllib3.PoolManager()
    url = sehir2
    response = http.request('GET', url)
    soup = BeautifulSoup(response.data,'lxml')

 
    
    
    
    dfff=pd.read_html(sehir2)
    saatler2 = []
    
    for table in soup.findAll('div', attrs={'class': 'race-block__time'}):
        for td in table.findAll('ul', attrs={'class': None}):
            for a in td.findAll('a', attrs={'class': None}):
                    saatler2.append(a['href'])
    for b in range(0, len(saatler2)):
        df2 = pd.read_html(saatler2[b])
        tarih2=[]
        for table in soup.findAll('table', attrs={'class': 'table-format-normal perfomance-border perfomance-table-style'}):
            for td in table.findAll('td', attrs={'class':None}):
                for a in td.findAll('a', attrs={'class': None}):
                    tarih2.append(a['href'])
        ss2=[]
        for t in range(0,len(tarih2)):
            df3=pd.read_html(tarih2[t])
            
            
            
            o=list(df3[0]['H.P'].values)
                #o.sort()
            ss2.append(o)
                   

            deneme2 = []
        for j in range(0,len(df2)):
                    
            
            for k in range(1, len(df2[j])):
                tot=len(df2[j])+len(df2[j-1])
                       
                if j%2==0:
                        continue
                if len(df2[j].values[0])<8:
                         continue
                    
                if j==1:
                    d=({'Tarih': df2[j].values[k][1:][0], 'Sehir': df2[j].values[k][2:][0],
                        'Şart:': df2[j].values[k][3:][0], 'Pist': df2[j].values[k][4:][0],
                        'PD': df2[j].values[k][5:][0], 'KG': df2[j].values[k][6:][0],
                        'Jokey': df2[j].values[k][7:][0], 'SN': df2[j].values[k][8:][0],
                        'S/K': df2[j].values[k][9:][0], 'Derece': df2[j].values[k][10:][0],
                        'Takı': df2[j].values[k][11:][0], 'D/800': df2[j].values[k][12:][0],
                        'Tabela & B. Farkları': df2[j].values[k][13:][0], 'AGF': df2[j].values[k][14:][0],
                        'H.P': df2[j].values[k][15:][0], 'İkr': df2[j].values[k][16:][0],'yarış saati':b ,'Tablo':j,'Geçmiş H.P':ss2[len(df2[j]):][k-1]})
           
                    
                        
                        
              
                    
                d=({'Tarih': df2[j].values[k][1:][0], 'Sehir': df2[j].values[k][2:][0],
                        'Şart:': df2[j].values[k][3:][0], 'Pist': df2[j].values[k][4:][0],
                        'PD': df2[j].values[k][5:][0], 'KG': df2[j].values[k][6:][0],
                        'Jokey': df2[j].values[k][7:][0], 'SN': df2[j].values[k][8:][0],
                        'S/K': df2[j].values[k][9:][0], 'Derece': df2[j].values[k][10:][0],
                        'Takı': df2[j].values[k][11:][0], 'D/800': df2[j].values[k][12:][0],
                        'Tabela & B. Farkları': df2[j].values[k][13:][0], 'AGF': df2[j].values[k][14:][0],
                        'H.P': df2[j].values[k][15:][0], 'İkr': df2[j].values[k][16:][0],'yarış saati':b ,'Tablo':j,'Geçmiş H.P':ss2[tot:][k]})
           
                deneme2.append(d)
    
        deneme2 = pd.DataFrame(deneme2)
        ad2 = 'şehir2 yaris{0}.xlsx'.format(b)
        ad2 = str(ad2)
        writer2 = pd.ExcelWriter(ad2)
        deneme2.to_excel(writer2,'Sheet{0}')  
        writer2.save()

program()    
program2()
