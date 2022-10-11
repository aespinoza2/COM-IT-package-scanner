import PyPDF2.pagerange
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDIconButton
from kivymd.uix.button import MDFlatButton
from kivy.core.window import Window
from kivy.config import Config
import requests
from bs4 import BeautifulSoup
from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path
import re
import urllib.request
import mechanize
from http.cookiejar import CookieJar


class LapWindow(Screen):
    pass
class DeskWindow(Screen):
    pass
class MonWindow(Screen):
    pass
class KeyWindow(Screen):
    pass
class DockWindow(Screen):
    pass
class PrintWindow(Screen):
    pass
class PackSlipScanWindow(Screen):
    pass
class PackSlipReadWindow(Screen):
    pass
class WindowManager(ScreenManager):
    pass

class PackageScanner(MDApp):
    def build(self):
        self.title = 'COM IT Asset Tracking Management System 1.0.0'
        kv = Builder.load_file('main.kv')
        Config.set('input', 'mouse', 'mouse, multitouch_on_demand')
        Window.size = (900, 500)
        return kv

    def macProcess(self):
        # Laptop codes
        lapTrackNum = self.root.get_screen('lapWin').ids.trackIn.text
        lapOrderNum = self.root.get_screen('lapWin').ids.orderIn.text
        lapTicketNum = self.root.get_screen('lapWin').ids.ticketIn.text
        lapSerialNum = self.root.get_screen('lapWin').ids.serialIn.text
        lapMacNum = self.root.get_screen('lapWin').ids.macIn.text
        lapTagNum = self.root.get_screen('lapWin').ids.tagIn.text
        if len(lapTrackNum) > 18:
            lapTrackNum = lapTrackNum[-11:]
            self.root.get_screen('lapWin').ids.trackIn.text = lapTrackNum
        if len(lapTicketNum) > 10:
            lapTicketNum = lapTicketNum[-10:]
            self.root.get_screen('lapWin').ids.ticketIn.text = lapTicketNum
        if len(lapMacNum) == 12:
            newLapMacNum = '-'.join(lapMacNum[i:i + 2] for i in range(0, len(lapMacNum), 2))
            self.root.get_screen('lapWin').ids.macIn.text = newLapMacNum
        # Desktop codes
        deskTrackNum = self.root.get_screen('deskWin').ids.trackIn.text
        deskOrderNum = self.root.get_screen('deskWin').ids.orderIn.text
        deskTicketNum = self.root.get_screen('deskWin').ids.ticketIn.text
        deskSerialNum = self.root.get_screen('deskWin').ids.serialIn.text
        deskMacNum = self.root.get_screen('deskWin').ids.macIn.text
        deskTagNum = self.root.get_screen('deskWin').ids.tagIn.text
        if len(deskTrackNum) > 18:
            deskTrackNum = deskTrackNum[-11:]
            self.root.get_screen('deskWin').ids.trackIn.text = deskTrackNum
        if len(deskTicketNum) > 10:
            deskTicketNum = deskTicketNum[-10:]
            self.root.get_screen('deskWin').ids.ticketIn.text = deskTicketNum
        if len(deskMacNum) == 12:
            newDeskMacNum = '-'.join(deskMacNum[i:i + 2] for i in range(0, len(deskMacNum), 2))
            self.root.get_screen('deskWin').ids.macIn.text = newDeskMacNum
        # Printer codes
        pTrackNum = self.root.get_screen('printWin').ids.trackIn.text
        pOrderNum = self.root.get_screen('printWin').ids.orderIn.text
        pTicketNum = self.root.get_screen('printWin').ids.ticketIn.text
        pSerialNum = self.root.get_screen('printWin').ids.serialIn.text
        pMacNum = self.root.get_screen('printWin').ids.macIn.text
        pTagNum = self.root.get_screen('printWin').ids.tagIn.text
        if len(pTrackNum) > 18:
            pTrackNum = pTrackNum[-11:]
            self.root.get_screen('printWin').ids.trackIn.text = pTrackNum
        if len(pTicketNum) > 10:
            pTicketNum = pTicketNum[-10:]
            self.root.get_screen('printWin').ids.ticketIn.text = pTicketNum
        if len(pMacNum) == 12:
            newPMacNum = '-'.join(pMacNum[i:i + 2] for i in range(0, len(pMacNum), 2))
            self.root.get_screen('printWin').ids.macIn.text = newPMacNum
        # Dock codes
        dockTrackNum = self.root.get_screen('dockWin').ids.trackIn.text
        dockOrderNum = self.root.get_screen('dockWin').ids.orderIn.text
        dockTicketNum = self.root.get_screen('dockWin').ids.ticketIn.text
        dockSerialNum = self.root.get_screen('dockWin').ids.serialIn.text
        dockMacNum = self.root.get_screen('dockWin').ids.macIn.text
        dockTagNum = self.root.get_screen('dockWin').ids.tagIn.text
        if len(dockTrackNum) > 18:
            dockTrackNum = dockTrackNum[-11:]
            self.root.get_screen('dockWin').ids.trackIn.text = dockTrackNum
        if len(dockTicketNum) > 10:
            dockTicketNum = dockTicketNum[-10:]
            self.root.get_screen('dockWin').ids.ticketIn.text = dockTicketNum
        if len(dockMacNum) == 12:
            newDockMacNum = '-'.join(dockMacNum[i:i + 2] for i in range(0, len(dockMacNum), 2))
            self.root.get_screen('dockWin').ids.macIn.text = newDockMacNum
        return self

    def noMacProcess(self):
        # Keyboard codes
        keyTrackNum = self.root.get_screen('keyWin').ids.trackIn.text
        keyOrderNum = self.root.get_screen('keyWin').ids.orderIn.text
        keyTicketNum = self.root.get_screen('keyWin').ids.ticketIn.text
        keySerialNum = self.root.get_screen('keyWin').ids.serialIn.text
        keyTagNum = self.root.get_screen('keyWin').ids.tagIn.text
        if len(keyTrackNum) > 18:
            keyTrackNum = keyTrackNum[-11:]
            self.root.get_screen('keyWin').ids.trackIn.text = keyTrackNum
        if len(keyTicketNum) > 10:
            keyTicketNum = keyTicketNum[-10:]
            self.root.get_screen('keyWin').ids.ticketIn.text = keyTicketNum
        # Monitor codes
        monTrackNum = self.root.get_screen('monWin').ids.trackIn.text
        monOrderNum = self.root.get_screen('monWin').ids.orderIn.text
        monTicketNum = self.root.get_screen('monWin').ids.ticketIn.text
        monSerialNum = self.root.get_screen('monWin').ids.serialIn.text
        monTagNum = self.root.get_screen('monWin').ids.tagIn.text
        if len(monTrackNum) > 18:
            monTrackNum = monTrackNum[-11:]
            self.root.get_screen('monWin').ids.trackIn.text = monTrackNum
        if len(monTicketNum) > 10:
            monTicketNum = monTicketNum[-10:]
            self.root.get_screen('monWin').ids.ticketIn.text = monTicketNum

    def packSlip(self):
        slipAddress = self.root.get_screen('packSlipScanWin').ids.slipAddress.text
        slipAddress = slipAddress + ".pdf"
        r = requests.get(slipAddress)
        pdf_filename = "PackSlip.pdf"
        open(pdf_filename, 'wb').write(r.content)
        input_pdf = PdfFileReader(pdf_filename)
        for page in input_pdf.pages:
            page_num = page
            #page_object = input_pdf.getPage(page_num)
            page_text = page.extractText()
            if 'ITEM DESCRIPTION' in page_text:
                pdf_item_list = re.split(r'\W+', page_text)
                item_index = pdf_item_list.index("QUANTITY")
                psItemDesc = pdf_item_list[item_index+1] + " " + pdf_item_list[item_index+2]
                self.root.get_screen('packSlipReadWin').ids.itemDesc.text = psItemDesc
            if 'PO Number' in page_text:
                pdf_ticket_list = re.split(r'\W+', page_text)
                ticket_index = pdf_ticket_list.index("PO")
                psTicketNum = pdf_ticket_list[ticket_index+2]
                self.root.get_screen('packSlipReadWin').ids.ticketIn.text = psTicketNum
                if len(psTicketNum) > 10:
                    psTicketNum = psTicketNum[3:13]
                    self.root.get_screen('packSlipReadWin').ids.ticketIn.text = psTicketNum
            if 'Order' in page_text:
                pdf_order_list = re.split(r'\W+', page_text)
                psOrderNum = pdf_order_list[1]
                self.root.get_screen('packSlipReadWin').ids.orderIn.text = psOrderNum
            if 'Shipped with' in page_text:
                pdf_track_list = re.split(r'\W+', page_text)
                track_index = pdf_track_list.index("with")
                psTrackNum = pdf_track_list[track_index+2]
                self.root.get_screen('packSlipReadWin').ids.trackIn.text = psTrackNum
            if 'Service Tags' in page_text:
                pdf_service_list = re.split(r'\W+', page_text)
                service_index = pdf_service_list.index("Tags")
                psServiceNum = pdf_service_list[service_index + 2]
                self.root.get_screen('packSlipReadWin').ids.serialIn.text = psServiceNum

    def comHelp(self):
        cookies = {
            '_fbp': 'fb.1.1581988650559.378115455',
            '__zlcmid': 'ztjOKgtHe8DMMk',
            'nmstat': 'd0d7a9bb-f055-238c-84e1-8517b92c6fa4',
            'mbox': 'PC#830742d037a24b3fb90a01d83801e00e.35_0#1695011868|session#8e3f41529f1a4caaa9d785939390d6b1#1631767827',
            'AMCV_4D6368F454EC41940A4C98A6%40AdobeOrg': '1075005958%7CMCIDTS%7C18887%7CMCMID%7C64930343654099489602905404502578150639%7CMCAAMLH-1632371870%7C9%7CMCAAMB-1632371870%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1631774270s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.4.1%7CMCCIDH%7C832639859',
            's_pers': '%20c19%3Dknovel%2520pi%253Aviewer%253Akhtml%253Aother%253A15%2520viewer%2520page%7C1631768999421%3B%20v68%3D1631767069362%7C1631768999437%3B%20v8%3D1631767243091%7C1726375243091%3B%20v8_s%3DLess%2520than%25201%2520day%7C1631769043091%3B',
            '_lo_uid': '139917-1634884773461-cbda139ccb69cb01',
            '_lo_v': '1',
            '_ga_823V87NG21': 'GS1.1.1634884769.1.0.1634884771.58',
            '_scid': 'e5e059bd-41ff-497b-bc3c-07bcad00e8d3',
            'LPVID': 'E3NWZhMmMyNGJjMDg2MmM0',
            'fpestid': 'sV9_hsnKUagCTKuquESEgugcfSzjm73E8ozY7zKdUyybKhPq4LDZPGXXMoNqTfp2PCs1Mg',
            '_hjSessionUser_1884950': 'eyJpZCI6IjBjNDE1MjY5LTllMmUtNTQ3Mi1iNzQ0LWY3ODAxNTJhNmVjNCIsImNyZWF0ZWQiOjE2NDAyMjA2MTE5NjgsImV4aXN0aW5nIjp0cnVlfQ==',
            '_tt_enable_cookie': '1',
            '_ttp': 'aef31854-4064-4a53-95e6-dbdbece9f2cd',
            '_ga_4HFV0NPHXM': 'GS1.1.1652822831.3.1.1652822967.0',
            '_gcl_dc': 'GCL.1654149233.Cj0KCQjwnNyUBhCZARIsAI9AYlHIe2b8imlKNzNVZxqwkS0tHp1r42CBmRyB2G-uTM96ECj3cninWxwaAoChEALw_wcB',
            '_gac_UA-66594374-45': '1.1654149233.Cj0KCQjwnNyUBhCZARIsAI9AYlHIe2b8imlKNzNVZxqwkS0tHp1r42CBmRyB2G-uTM96ECj3cninWxwaAoChEALw_wcB',
            '_rdt_uuid': '1654149232945.4aa6bef4-30fb-4033-a9c6-7c21acaef821',
            '_gac_UA-66594374-16': '1.1654149233.Cj0KCQjwnNyUBhCZARIsAI9AYlHIe2b8imlKNzNVZxqwkS0tHp1r42CBmRyB2G-uTM96ECj3cninWxwaAoChEALw_wcB',
            '_ce.s': 'v11.rlc~1654149233881~v~d31e1cd9eacf7c60064760e8516385fb7996bd47~vpv~0',
            '_ga_274490789': 'GS1.1.1654722421.4.0.1654722434.0',
            '_ga_Z7M1CQR5R9': 'GS1.1.1655201612.1.0.1655201612.0',
            '_hjSessionUser_2604608': 'eyJpZCI6IjZhY2FkMGJhLWM4OGUtNTdhZi1iMGVhLTJjY2JjZDRhZDcwYiIsImNyZWF0ZWQiOjE2NTUyMDE2MTI2NDgsImV4aXN0aW5nIjpmYWxzZX0=',
            '_gcl_au': '1.1.981539736.1655315562',
            '_sctr': '1|1655881200000',
            '_gcl_aw': 'GCL.1655938352.CjwKCAjw-8qVBhANEiwAfjXLrvxI7JODzcBvqUAO7Ej7hn1RbVkTCx__puBBNZBXlmca05i22AiBlRoCx0sQAvD_BwE',
            '_uetvid': '2d7391302caf11eca3b0d58c86fb5425',
            '_ga_L0GHQS8E31': 'GS1.1.1655938351.1.1.1655938400.0',
            '_ga_7PV3540XS3': 'GS1.1.1655941132.82.1.1655941159.33',
            '_gid': 'GA1.2.1963812643.1656204361',
            '_ga_D910L0L5N2': 'GS1.1.1656604155.108.0.1656604155.0',
            '_ga': 'GA1.2.1253769109.1575330124',
            'PHPSESSID': 'voqko3a147rcbrdhql09g9ili9',
        }

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            # Requests sorts cookies= alphabetically
            # 'Cookie': '_fbp=fb.1.1581988650559.378115455; __zlcmid=ztjOKgtHe8DMMk; nmstat=d0d7a9bb-f055-238c-84e1-8517b92c6fa4; mbox=PC#830742d037a24b3fb90a01d83801e00e.35_0#1695011868|session#8e3f41529f1a4caaa9d785939390d6b1#1631767827; AMCV_4D6368F454EC41940A4C98A6%40AdobeOrg=1075005958%7CMCIDTS%7C18887%7CMCMID%7C64930343654099489602905404502578150639%7CMCAAMLH-1632371870%7C9%7CMCAAMB-1632371870%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1631774270s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.4.1%7CMCCIDH%7C832639859; s_pers=%20c19%3Dknovel%2520pi%253Aviewer%253Akhtml%253Aother%253A15%2520viewer%2520page%7C1631768999421%3B%20v68%3D1631767069362%7C1631768999437%3B%20v8%3D1631767243091%7C1726375243091%3B%20v8_s%3DLess%2520than%25201%2520day%7C1631769043091%3B; _lo_uid=139917-1634884773461-cbda139ccb69cb01; _lo_v=1; _ga_823V87NG21=GS1.1.1634884769.1.0.1634884771.58; _scid=e5e059bd-41ff-497b-bc3c-07bcad00e8d3; LPVID=E3NWZhMmMyNGJjMDg2MmM0; fpestid=sV9_hsnKUagCTKuquESEgugcfSzjm73E8ozY7zKdUyybKhPq4LDZPGXXMoNqTfp2PCs1Mg; _hjSessionUser_1884950=eyJpZCI6IjBjNDE1MjY5LTllMmUtNTQ3Mi1iNzQ0LWY3ODAxNTJhNmVjNCIsImNyZWF0ZWQiOjE2NDAyMjA2MTE5NjgsImV4aXN0aW5nIjp0cnVlfQ==; _tt_enable_cookie=1; _ttp=aef31854-4064-4a53-95e6-dbdbece9f2cd; _ga_4HFV0NPHXM=GS1.1.1652822831.3.1.1652822967.0; _gcl_dc=GCL.1654149233.Cj0KCQjwnNyUBhCZARIsAI9AYlHIe2b8imlKNzNVZxqwkS0tHp1r42CBmRyB2G-uTM96ECj3cninWxwaAoChEALw_wcB; _gac_UA-66594374-45=1.1654149233.Cj0KCQjwnNyUBhCZARIsAI9AYlHIe2b8imlKNzNVZxqwkS0tHp1r42CBmRyB2G-uTM96ECj3cninWxwaAoChEALw_wcB; _rdt_uuid=1654149232945.4aa6bef4-30fb-4033-a9c6-7c21acaef821; _gac_UA-66594374-16=1.1654149233.Cj0KCQjwnNyUBhCZARIsAI9AYlHIe2b8imlKNzNVZxqwkS0tHp1r42CBmRyB2G-uTM96ECj3cninWxwaAoChEALw_wcB; _ce.s=v11.rlc~1654149233881~v~d31e1cd9eacf7c60064760e8516385fb7996bd47~vpv~0; _ga_274490789=GS1.1.1654722421.4.0.1654722434.0; _ga_Z7M1CQR5R9=GS1.1.1655201612.1.0.1655201612.0; _hjSessionUser_2604608=eyJpZCI6IjZhY2FkMGJhLWM4OGUtNTdhZi1iMGVhLTJjY2JjZDRhZDcwYiIsImNyZWF0ZWQiOjE2NTUyMDE2MTI2NDgsImV4aXN0aW5nIjpmYWxzZX0=; _gcl_au=1.1.981539736.1655315562; _sctr=1|1655881200000; _gcl_aw=GCL.1655938352.CjwKCAjw-8qVBhANEiwAfjXLrvxI7JODzcBvqUAO7Ej7hn1RbVkTCx__puBBNZBXlmca05i22AiBlRoCx0sQAvD_BwE; _uetvid=2d7391302caf11eca3b0d58c86fb5425; _ga_L0GHQS8E31=GS1.1.1655938351.1.1.1655938400.0; _ga_7PV3540XS3=GS1.1.1655941132.82.1.1655941159.33; _gid=GA1.2.1963812643.1656204361; _ga_D910L0L5N2=GS1.1.1656604155.108.0.1656604155.0; _ga=GA1.2.1253769109.1575330124; PHPSESSID=voqko3a147rcbrdhql09g9ili9',
            'Referer': 'https://comhelp.arizona.edu/index.php',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        lapTicketNum = self.root.get_screen('lapWin').ids.ticketIn.text
        response = requests.get('https://comhelp.arizona.edu/tech/search.php?keywords=' + lapTicketNum, cookies=cookies, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        print("----THIS IS THE TICKET SEARCH PAGE----")
        print(soup.prettify())

        links = []
        for hypLink in soup.find_all('a'):
            links.append(hypLink.get('href'))
        print("---THESE ARE THE LINKS---")
        print(links)
        new_response = requests.get(links[27], cookies=cookies, headers=headers)
        ticket_soup = BeautifulSoup(new_response.content, 'html.parser')
        print(ticket_soup.prettify())



if __name__ == '__main__':
    PackageScanner().run()
