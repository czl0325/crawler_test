import ssl
import requests
import re

ssl._create_default_https_context = ssl._create_unverified_context

headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
    "cookie":"BAIDUID=80F63AA8B77782EFF75E057C41839530:FG=1; BIDUPSID=80F63AA8B77782EFF75E057C41839530; PSTM=1553868593; BDUSS=A1NVlFdGhjMlgtc2tuYlNmZHI0fnFFeGhRbzZ5RVlxWVN1OWMxUX5yaVlKRDFlSVFBQUFBJCQAAAAAAAAAAAEAAABEFRZQs8LV0cG8MTk4MzAzMjUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJiXFV6YlxVeNn; lscaptain=srcactivitycaptainindexcss_91e010cf-srccommonlibsesljs_e3d2f596-srcactivitycaptainindexjs_a2e9c712; Hm_lvt_68bd357b1731c0f15d8dbfef8c216d15=1582621278,1582680583; Hm_lpvt_68bd357b1731c0f15d8dbfef8c216d15=1582681989; H_PS_PSSID=30744_1454_21084_30841_30824_26350; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=6; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598"
}


response = requests.get('https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_pc_3', headers=headers)
html_str = response.content.decode('utf-8')
print(html_str)

result = re.findall(r'<div class="VirusSummarySix_1-1-190_3haLBF VirusSummarySix_1-1-190_2ZJJBJ">(\d+)</div>', html_str)
print(result)

# <div class="VirusSummarySix_1-1-190_3haLBF VirusSummarySix_1-1-190_2ZJJBJ">47313</div>
# <div class="VirusSummarySix_1-1-190_3haLBF VirusSummarySix_1-1-190_2ZJJBJ">2824</div>