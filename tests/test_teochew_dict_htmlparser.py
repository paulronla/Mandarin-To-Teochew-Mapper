import sys
sys.path.append('../.')
import unittest
import json
from teochew_dict_htmlparser import TeochewDictHTMLParser


class TestTeochewDictHTMLParser(unittest.TestCase):
    def test_get_teochew_dict(self):
        parser = TeochewDictHTMLParser()
        parser.feed('''<dl>
                <dt>
                  <p>片</p>	
                </dt>
                <dd><ul>
  	    
 		            <li><b>潮州音：</b>[piêng3 骗]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/EC307987-8B0D-46B6-87DD-56201CC31482.mp3" ></button>
     
     </li>
 		
 		            <li><b>汕头音：</b>[piang3 骗]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/E94C598E-552B-469B-B4D5-73FDF87D72F4.mp3" ></button>
     
     </li>
 		
 		            <li><b>揭阳音：</b>[piang3 骗]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/E94C598E-552B-469B-B4D5-73FDF87D72F4.mp3" ></button>
     
     </li>
 		
 		            <li><b>澄海音：</b>[piang3 骗]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/E94C598E-552B-469B-B4D5-73FDF87D72F4.mp3" ></button>
     
     </li>
 		
 		            <li><b>潮阳音：</b>[piang3 骗]
 		
     </li>
 		
 		            <li><b>潮州音：</b>[pin3 颇燕]（白）
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/6FE29C11-E1C0-4B7F-B6B8-8E3B73B119F7.mp3" ></button>
     
     </li>
 		
 		            <li><b>拼    音：</b>piàn  <button class="laba2"  role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/pth/14F9EE84-01F6-42AC-8E0C-0DBD45EFFBAD.mp3"></button></li>
 		
 		            <li><b>拼    音：</b>piān  <button class="laba2"  role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/pth/60319F66-89E0-4778-A50C-6AB7C56F0115.mp3"></button></li>
 		
                    <li><b>字    义：</b>1.piàn||piêng3|piang3 ①平而薄的物体：明信~|铁~子。②切削成薄片：~肉片|把豆腐干~一~。③少，零星：~言|~纸只字|~刻。④量词，指面积、范围或成片的东西：一大~绿油油的庄稼|一~草地|两~儿药。 2.pin3 ①<潮>一半门户等：一~门|一~窗。②<潮>边，面：只~（这边）|许~（那边）。 3.piān||piêng3|piang3 同“1.①”，用于相片儿、画片儿、唱片儿、电影片儿等。</li>
                    
                </ul>
                </dd>
             </dl>''')
        self.assertEqual(parser.get_teochew_dict(),
                        {'片': {'pian4': 'piang3|pin3(白)', 'pian1': 'piang3'}})
        self.assertEqual(parser.get_chaoyin_audio_map(),
                        {'piêng3': 'EC307987-8B0D-46B6-87DD-56201CC31482',
                        'piang3': 'E94C598E-552B-469B-B4D5-73FDF87D72F4',
                        'pin3': '6FE29C11-E1C0-4B7F-B6B8-8E3B73B119F7'})
        parser = TeochewDictHTMLParser()
        parser.feed('''<dl>
                <dt>
                  <p>亡</p>	
                </dt>
                <dd><ul>
  	    
 		            <li><b>潮州音：</b>[bhuang5 忘5]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/82B4432A-D418-4275-BEAA-04A8738BE89C.mp3" ></button>
     
     </li>
 		
 		            <li><b>汕头音：</b>[mang5 忙]（又）
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/65B079C8-F41A-438E-BFAD-67BFA18A70A4.mp3" ></button>
     
     </li>
 		
 		            <li><b>潮州音：</b>[bho5 无]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/0DC6FD41-4584-4BB0-B575-4DC0F9C3AAF1.mp3" ></button>
     
     </li>
 		
 		            <li><b>拼    音：</b>wáng  <button class="laba2"  role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/pth/56B18CF0-C209-4D13-8BBE-FD242E686EFE.mp3"></button></li>
 		
 		            <li><b>拼    音：</b>wú  <button class="laba2"  role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/pth/44D35633-E617-46BF-9D85-B56E8835FE6C.mp3"></button></li>
 		
                    <li><b>字    义：</b>|1.wáng||bhuang5|汕（又）mang5 ①逃：~命|流~。②失去：~羊补牢|~魂丧胆。③死：伤~很少。④死去的：~弟。⑤灭：~国|唇~齿寒。 2.wú||bho5 古同“无”。</li>
                    
                </ul>
                </dd>
             </dl>''')
        self.assertEqual(parser.get_teochew_dict(),
                        {'亡': {'wang2': 'bhuang5|mang5(汕)(又)', 'wu2': 'bho5'}})
        self.assertEqual(parser.get_chaoyin_audio_map(),
                        {'bhuang5': '82B4432A-D418-4275-BEAA-04A8738BE89C',
                        'mang5': '65B079C8-F41A-438E-BFAD-67BFA18A70A4',
                        'bho5': '0DC6FD41-4584-4BB0-B575-4DC0F9C3AAF1'})
        parser = TeochewDictHTMLParser()
        parser.feed('''<dl>
                <dt>
                  <p>张</p>	
                </dt>
                <dd>

                <ul>
  	    
 		            <li><b>繁异体：</b>張</li>
 		
 		            <li><b>潮州音：</b>[diên1 场1]（白）（姓）
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/DB9E8364-07F3-45E5-AB9B-C56612C8F45C.mp3" ></button>
     
     </li>
 		
 		            <li><b>汕头音：</b>[dion1 场1]（白）（姓）
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/33730461-A0AA-44CA-88DD-035681ED93F3.mp3" ></button>
     
     </li>
 		
 		            <li><b>揭阳音：</b>[dion1 场1]（白）（姓）
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/33730461-A0AA-44CA-88DD-035681ED93F3.mp3" ></button>
     
     </li>
 		
 		            <li><b>潮阳音：</b>[dion1 场1]（白）（姓）
 		
     </li>
 		
 		            <li><b>潮州音：</b>[ziang1 彰]（文）
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/3014D5B2-C49F-47D5-953C-80166E558C44.mp3" ></button>
     
     </li>
 		
 		            <li><b>潮州音：</b>[diên3 帐]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/11DF9E89-2871-47A2-B32A-9CD9D1EE8368.mp3" ></button>
     
     </li>
 		
 		            <li><b>汕头音：</b>[dion3 帐]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/99CDF1A4-8B01-4EC9-AB69-C247E1FEC392.mp3" ></button>
     
     </li>
 		
 		            <li><b>揭阳音：</b>[dion3 帐]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/99CDF1A4-8B01-4EC9-AB69-C247E1FEC392.mp3" ></button>
     
     </li>
 		
 		            <li><b>潮阳音：</b>[dion3 帐]
 		
     </li>
 		
 		            <li><b>拼    音：</b>zhāng  <button class="laba2"  role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/pth/32C8FCB3-B67E-455A-A81A-A4B7B25FEF67.mp3"></button></li>
 		
                    <li><b>字    义：</b>1.zhāng||diên1|dion1|ziang1 ①开，展开：~嘴|~牙舞爪|~网捕鱼。②扩大，夸大：虚~声势|~大其词。③放纵，无拘束：乖~|嚣~。④绷紧，紧迫：一~一弛|紧~。⑤商店开业：开~|新~大喜。⑥看，望：东~西望。⑦量词，用于弓、嘴和其他带有平面的东西：一~弓|两~纸。⑧星宿名，二十八宿之一。⑨姓。⑩<潮>张设机关捕捉：~鸟|~老鼠。⑪<潮>设局算计人：~人~家己（算计人到头来算计了自己）。⑫<潮>不真实，假装：~样|~形|伊肚痛个~个（他肚子疼是装出来的）。 2.diên3|dion3 ①<潮>眼睛、嘴巴等的开合动作：目~金（眼睛张开）|嘴~眯（嘴闭拢）。②头、手、脚抬高或身体、手、脚移动的动作：头~危[guin5]（头抬高）|手~浮（手抬高）|脚~开（脚挪开）|人~好（人挪一挪）。</li>
                    
                </ul>
                </dd>
             </dl>
             <dl>
                <dt>
                  <p>掀</p>	
                </dt>
                <dd>

                <ul>
  	    
 		            <li><b>潮州音：</b>[hiêng1 显1]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/97BF937E-B67F-4296-BA15-E4211F772B67.mp3" ></button>
     
     </li>
 		
 		            <li><b>汕头音：</b>[hiang1 香]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/D91D50C8-DA39-4702-93AA-F5748822D2B7.mp3" ></button>
     
     </li>
 		
 		            <li><b>揭阳音：</b>[hiang1 香]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/D91D50C8-DA39-4702-93AA-F5748822D2B7.mp3" ></button>
     
     </li>
 		
 		            <li><b>澄海音：</b>[hiang1 香]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/D91D50C8-DA39-4702-93AA-F5748822D2B7.mp3" ></button>
     
     </li>
 		
 		            <li><b>潮阳音：</b>[hiang1 香]
 		
     </li>
 		
 		            <li><b>潮州音：</b>[hng1 欣]（又）
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/42319BC2-E536-4ED1-8B0B-13DA182ACB02.mp3" ></button>
     
     </li>
 		
 		            <li><b>汕头音：</b>[heng1 欣]（又）
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/8099DE85-F234-4760-B5DC-A4A4322EB006.mp3" ></button>
     
     </li>
 		
 		            <li><b>澄海音：</b>[heng1 欣]（又）
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/8099DE85-F234-4760-B5DC-A4A4322EB006.mp3" ></button>
     
     </li>
 		
 		            <li><b>揭阳音：</b>[hêng1 欣]（又）
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/E93587E9-3EA7-4BFA-9DBC-B9BC3823012B.mp3" ></button>
     
     </li>
 		
 		            <li><b>潮州音：</b>[hioun1 枭（鼻化）]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/34A848D2-D73C-477E-A763-FF30D644E15A.mp3" ></button>
     
     </li>
 		
 		            <li><b>汕头音：</b>[hiaon1 枭（鼻化）]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/BC90D80B-4040-4F04-83B0-12AAE469F0A2.mp3" ></button>
     
     </li>
 		
 		            <li><b>揭阳音：</b>[hiaon1 枭（鼻化）]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/BC90D80B-4040-4F04-83B0-12AAE469F0A2.mp3" ></button>
     
     </li>
 		
 		            <li><b>潮阳音：</b>[hiaon1 枭（鼻化）]
 		
     </li>
 		
 		            <li><b>拼    音：</b>xiān  <button class="laba2"  role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/pth/5EC53669-7DA3-4586-AAA3-2D1520D618B6.mp3"></button></li>
 		
                    <li><b>字    义：</b>1.xiān||hiêng1|hiang1|hng1|heng1 ①揭起，打开：~锅盖|~帘子。②发动，兴起：~起高潮。 2.xiān||hioun1|hiaon1 翻起，翻开：~书。</li>

                </ul>
                </dd>
             </dl>''')
        self.assertEqual(parser.get_teochew_dict(), {
                        '张': {'zhang1': 'dion1(白)(姓)|ziang1(文)|dion3'}, 
                        '掀': {'xian1':'hiang1|hng1(又)|heng1(汕)(又)|hiaon1'}
                        })
        self.assertEqual(parser.get_chaoyin_audio_map(), {
                        'diên1': 'DB9E8364-07F3-45E5-AB9B-C56612C8F45C',
                        'dion1': '33730461-A0AA-44CA-88DD-035681ED93F3', 
                        'ziang1': '3014D5B2-C49F-47D5-953C-80166E558C44', 
                        'diên3': '11DF9E89-2871-47A2-B32A-9CD9D1EE8368', 
                        'dion3': '99CDF1A4-8B01-4EC9-AB69-C247E1FEC392', 
                        'hiêng1': '97BF937E-B67F-4296-BA15-E4211F772B67', 
                        'hiang1': 'D91D50C8-DA39-4702-93AA-F5748822D2B7', 
                        'hng1': '42319BC2-E536-4ED1-8B0B-13DA182ACB02', 
                        'heng1': '8099DE85-F234-4760-B5DC-A4A4322EB006', 
                        'hêng1': 'E93587E9-3EA7-4BFA-9DBC-B9BC3823012B', 
                        'hioun1': '34A848D2-D73C-477E-A763-FF30D644E15A', 
                        'hiaon1': 'BC90D80B-4040-4F04-83B0-12AAE469F0A2'
                        })
        parser = TeochewDictHTMLParser()
        parser.feed('''<dl>
                <dt>
                  <p>陂</p>	
                </dt>
                <dd><ul>
  	    
 		            <li><b>潮州音：</b>[bi1 碑]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/3D0E2B6F-2CB2-43B3-921C-67BF57005221.mp3" ></button>
     
     </li>
 		
 		            <li><b>潮州音：</b>[pi5 疲]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/735AC829-3E7E-4678-8953-70F3125720A1.mp3" ></button>
     
     </li>
 		
 		            <li><b>潮州音：</b>[po1 颇]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/38B944FB-F843-4ACD-BB56-F7B84B0C08B9.mp3" ></button>
     
     </li>
 		
 		            <li><b>汕头音：</b>[bo1 波]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/4CCEE68C-96BB-4181-B010-C751B9F845D3.mp3" ></button>
     
     </li>
 		
 		            <li><b>拼    音：</b>bēi  <button class="laba2"  role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/pth/B690357E-F525-4B13-8F9C-B0E3AE764490.mp3"></button></li>
 		
 		            <li><b>拼    音：</b>pí  <button class="laba2"  role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/pth/02B5C7D6-F017-411E-85E4-FBF205FE7731.mp3"></button></li>
 		
 		            <li><b>拼    音：</b>pō  <button class="laba2"  role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/pth/191F3105-D06D-4B60-B22B-08C753B96F8B.mp3"></button></li>
 		
                    <li><b>字    义：</b>1.bēi [bi1 碑] ①池塘：~塘|~池。②水边，岸。③山坡，坡地。 2.pí [pi5 疲] 【黄陂】地名，在湖北省。 3.pō [po1 颇] 汕[bo1 波] 【陂陀】不平坦。</li>
                    
                </ul>
                </dd>
             </dl>
                <dl>
                <dt>
                  <p>𫢗</p>	
                </dt>
                <dd><ul>
  	    
 		            <li><b>潮州音：</b>[diang5 多央5]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/067CCBCE-4107-438B-82D5-077FA86F5661.mp3" ></button>
     
     </li>
 		
                    <li><b>字    义：</b><方>谁。</li>
                    
                </ul>
                </dd>
             </dl>
                <dl>
                <dt>
                  <p>仆</p>	
                </dt>
                <dd><ul>
  	    
 		            <li><b>潮州音：</b>[pog4 扑]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/93751E84-E221-4CF8-9C9B-53D429C4D66C.mp3" ></button>
     
     </li>
 		
 		            <li><b>潮州音：</b>[bog8 卜8]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/520A501D-2C4E-4903-8E30-9517F618345E.mp3" ></button>
     
     </li>
 		
 		            <li><b>拼    音：</b>pū  <button class="laba2"  role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/pth/41F72013-897B-4D80-9711-8D6958F66120.mp3"></button></li>
 		
 		            <li><b>拼    音：</b>pú  <button class="laba2"  role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/pth/75658517-3516-4E73-9E71-9FF65CFEF602.mp3"></button></li>
 		
                    <li><b>字    义：</b>1.pū[pog4 扑] 向前跌倒：前~后继。2.pú[bog8 卜8] ①被雇到家里做杂事、供役使的人：~人|女~。②旧时男子谦称自己。③【仆仆】旅途劳累的样子：风尘~~。☞此义不读pū[pog4 扑]。</li>
                    
                </ul>
                </dd>
             </dl>
             <dl>
                <dt>
                  <p>鶪</p>	
                </dt>
                <dd><ul>
  	    
 		            <li><b>潮州音：</b>[gu6 具]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/21EB9444-7B1E-4364-A856-7B0281340072.mp3" ></button>
     
     </li>
 		
 		            <li><b>拼    音：</b>jú  <button class="laba2"  role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/pth/28505819-3F03-4FD3-9E0E-667B1C84C3FC.mp3"></button></li>
 		
                    <li><b>字    义：</b><span style="color:#ff0000">待添加。</span></li>
                    
                </ul>
                </dd>
             </dl>
             <dl>
                <dt>
                  <p>谁</p>	
                </dt>
                <dd>

                <ul>
  	    
 		            <li><b>潮州音：</b>[sui5 随]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/3D399B72-0C7F-491E-B8CF-D51568CE7189.mp3" ></button>
     
     </li>
 		
 		            <li><b>拼    音：</b>shuí  <button class="laba2"  role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/pth/15888753-A319-46A6-865A-94201573A347.mp3"></button></li>
 		
 		            <li><b>拼    音：</b>shéi  <button class="laba2"  role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/pth/292DFEFC-EE89-40A6-8459-E3B49C2791F4.mp3"></button></li>
 		
                    <li><b>字    义：</b>①疑问人称代词：~来啦？②任何人，无论什么人：~都可以做。</li>
                    
                </ul>
                </dd>
             </dl>
             <dl>
                <dt>
                  <p>熟</p>	
                </dt>
                <dd>

                <ul>
  	    
 		            <li><b>潮州音：</b>[sêg8 升8]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/C0C08FEE-9533-4856-8250-A8CA3F2FB1E9.mp3" ></button>
     
     </li>
 		
 		            <li><b>拼    音：</b>shú  <button class="laba2"  role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/pth/7DC492AB-2184-433B-9499-44F69C73802C.mp3"></button></li>
 		
 		            <li><b>拼    音：</b>shóu  <button class="laba2"  role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/pth/0E629F43-2519-4002-81AA-F186E00FA0E5.mp3"></button></li>
 		
                    <li><b>字    义：</b>1.shú||sêg8 ①食物烧煮到可吃的程度：饭~了|~菜。②成熟，植物的果实或种子长成：麦子~了。③程度深：深思~虑|~睡。④习惯，常见，知道清楚：~悉|~人|这条路我~。⑤熟练，做某种工作时间久了，精通而有经验：~手|~能生巧。⑥经过加工或炼制的：~铁|~皮子。 2.shóu||sêg8 义同“1”，用于口语。</li>
                    
                </ul>
                </dd>
             </dl>''')
        self.assertEqual(parser.get_teochew_dict(), {
                        '陂': {'bei1': 'bi1', 'pi2': 'pi5', 'po1': 'po1|bo1(汕)'}, 
                        '𫢗': {'': 'diang5'}, 
                        '仆': {'pu1': 'pog4', 'pu2': 'bog8'}, 
                        '鶪': {'ju2': 'gu6'}, 
                        '谁': {'shui2': 'sui5', 'shei2': 'sui5'}, 
                        '熟': {'shu2': 'sêg8', 'shou2': 'sêg8'}
                        })
        parser = TeochewDictHTMLParser()
        parser.feed('''<dl>
                <dt>
                  <p>贠</p>	
                </dt>
                <dd>

                <ul>
  	    
 		            <li><b>繁异体：</b>貟</li>
 		
 		            <li><b>潮州音：</b>[uêng5 完]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/450BF814-085C-47F6-88A7-A5C407F726D7.mp3" ></button>
     
     </li>
 		
 		            <li><b>汕头音：</b>[uang5 王]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/716FFCBD-5FDD-489A-9E89-A5CDA920A442.mp3" ></button>
     
     </li>
 		
 		            <li><b>揭阳音：</b>[uang5 王]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/716FFCBD-5FDD-489A-9E89-A5CDA920A442.mp3" ></button>
     
     </li>
 		
 		            <li><b>澄海音：</b>[uang5 王]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/716FFCBD-5FDD-489A-9E89-A5CDA920A442.mp3" ></button>
     
     </li>
 		
 		            <li><b>潮阳音：</b>[uang5 王]
 		
     </li>
 		
 		            <li><b>潮州音：</b>[ung7 运]（姓）
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/FA44A7CF-070D-4203-9221-B9CF235B1AF4.mp3" ></button>
     
     </li>
 		
 		            <li><b>拼    音：</b>yuán  <button class="laba2"  role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/pth/4F2D1A8F-EB4B-4399-93A9-E688A2981CA6.mp3"></button></li>
 		
 		            <li><b>拼    音：</b>yùn  <button class="laba2"  role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/pth/0269A9A4-2B92-4891-82AF-93AF745BA1D1.mp3"></button></li>
 		
                    <li><b>字    义：</b>1.yuán [uêng5 完][uang5 王] 古同“员”。2.yùn[ung7 运] 姓。唐代有贠半千。</li>
                </ul>
                </dd>
             </dl>
             <dl>
                <dt>
                  <p>渐</p>	
                </dt>
                <dd>

                <ul>
  	    
 		            <li><b>繁异体：</b>漸</li>
 		
 		            <li><b>潮州音：</b>[ziam6 尖6]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/B37AE409-962B-4F09-A0D9-EFDF1E748CD5.mp3" ></button>
     
     </li>
 		
 		            <li><b>澄海音：</b>[ziang6 尖6]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/DE03C987-02E3-4093-828A-002B379AD8CE.mp3" ></button>
     
     </li>
 		
 		            <li><b>潮州音：</b>[ziam1 尖]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/9EA15090-C256-477D-B599-BA80F7436C47.mp3" ></button>
     
     </li>
 		
 		            <li><b>澄海音：</b>[ziang1 尖]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/3014D5B2-C49F-47D5-953C-80166E558C44.mp3" ></button>
     
     </li>
 		
 		            <li><b>拼    音：</b>jiàn  <button class="laba2"  role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/pth/F538EE75-EB6C-4CF9-9097-FCB6088BA689.mp3"></button></li>
 		
 		            <li><b>拼    音：</b>jiān  <button class="laba2"  role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/pth/4D1D4E3A-BE95-46C0-A851-BEA37C61CACA.mp3"></button></li>
 		
                    <li><b>字    义：</b>㊀jiàn||ziam6|澄ziang6 ①副词，慢慢地，一点一点地：循序~进|~入佳境|他的病~~好了。②<书>苗头：防微杜~。㊁jiān||ziam1|澄ziang1 ①浸：~染（同于经常接触，自然而然地受到影响）。②流入：东~于海。</li>
                    
                </ul>
                </dd>
             </dl>
             <dl>
                <dt>
                  <p>嗳</p>	
                </dt>
                <dd>

                <ul>
  	    
 		            <li><b>繁异体：</b>噯</li>
 		
 		            <li><b>潮州音：</b>[ai3 哀3]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/1E838100-1A4D-4798-8E33-D3E385969868.mp3" ></button>
     
     </li>
 		
 		            <li><b>潮州音：</b>[an6 馅6]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/3785CA38-4826-4946-9872-38DFB6770D8E.mp3" ></button>
     
     </li>
 		
 		            <li><b>潮州音：</b>[ai7 哀7]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/B1CC2079-45AD-4E66-9509-918C4DC23D7E.mp3" ></button>
     
     </li>
 		
 		            <li><b>潮州音：</b>[ai1 哀]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/C3D71A4E-271D-4FAE-A1B7-7F48C01E7346.mp3" ></button>
     
     </li>
 		
 		            <li><b>拼    音：</b>ǎi  <button class="laba2"  role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/pth/1B4D805B-8618-4C0C-B809-B107F98F0FD9.mp3"></button></li>
 		
 		            <li><b>拼    音：</b>ài  <button class="laba2"  role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/pth/FE870030-3122-4BFF-AE61-67B4C7520A59.mp3"></button></li>
 		
 		            <li><b>拼    音：</b>āi  <button class="laba2"  role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/pth/01EEBC53-52B0-460D-AC2D-E54E702AF0AC.mp3"></button></li>
 		
                    <li><b>字    义：</b>①ǎi [ai3 哀3][an6 馅6] 叹词，表示否定或不同意：~，别那么说|~，不是这样放。
②ài [ai7 哀7] 叹词，表示懊恼、悔恨：~早知道是这样，我就不来了。
③āi [ai1 哀]同“哎”。</li>
                    
                </ul>
                </dd>
             </dl>
             <dl>
                <dt>
                  <p>赚</p>	
                </dt>
                <dd>

                <ul>
  	    
 		            <li><b>繁异体：</b>賺</li>
 		
 		            <li><b>潮州音：</b>[tang3 塘3]（俗）
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/72E42123-2841-449B-9379-DA2F28D474EB.mp3" ></button>
     
     </li>
 		
 		            <li><b>潮州音：</b>[zuang3 装3]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/9E863883-C316-4FFD-ABB2-FC2375D23B52.mp3" ></button>
     
     </li>
 		
 		            <li><b>拼    音：</b>zhuàn  <button class="laba2"  role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/pth/0312CCA7-06C3-4072-8350-DF0B6F61CC47.mp3"></button></li>
 		
 		            <li><b>拼    音：</b>zuàn  <button class="laba2"  role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/pth/C2C4F2D4-D8B9-4F34-AC77-91BDCFC6E69B.mp3"></button></li>
 		
                    <li><b>字    义：</b>㊀zhuàn[tang3 塘3]做买卖得利：~钱。㊁zuàn 诳骗：~人。</li>
                    
                </ul>
                </dd>
             </dl>
             <dl>
                <dt>
                  <p>个</p>	
                </dt>
                <dd><ul>
  	    
 		            <li><b>繁异体：</b>個</li>
 		
 		            <li><b>潮州音：</b>[gai5 介5]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/932484F2-94B7-455A-82EF-F27015F397DE.mp3" ></button>
     
     </li>
 		
 		            <li><b>潮州音：</b>[gai7 介7]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/37295302-7CCE-4AB2-85C5-0D56D2CDD288.mp3" ></button>
     
     </li>
 		
 		            <li><b>潮州音：</b>[go6 哥]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/758DA97E-4E52-429B-95FD-80971D11E233.mp3" ></button>
     
     </li>
 		
 		            <li><b>拼    音：</b>gè  <button class="laba2"  role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/pth/0AC415D7-9682-49B9-BE63-9C4D5D6CC2C9.mp3"></button></li>
 		
 		            <li><b>拼    音：</b>gě  <button class="laba2"  role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/pth/B9C28537-2C5F-4653-A3B3-A332C7044D20.mp3"></button></li>
 		
                    <li><b>字    义：</b>1.gè||gai5 ①量词：a.指一般单位的东西：三~月|一~人|五~苹果。b.指一次动作行为：一~不留神|给他~不理。c.<潮>货币单位，元：一斤三~（500 克 3 块钱）。②人或物的体积：高~子|小~儿|馒头~儿不小。 2.gè||go6 单独的：~人|~体。 3.gai7 <潮>①结构助词，同“的”：我~|红~。②对，跟，介词：~伊呾（跟他说）。</li>
                    
                </ul>
                </dd>
             </dl>
             <dl>
                <dt>
                  <p>二</p>	
                </dt>
                <dd>

                <ul>
  	    
 		            <li><b>大写字：</b>贰（貳）</li>

 		            <li><b>潮州音：</b>[no6 努6]（训）
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/13474AC5-39F6-4D36-8398-E6BA0B4EEDAB.mp3" ></button>
     
     </li>
 		
 		            <li><b>潮州音：</b>[ri6 字6]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/7DD84BF6-54FE-47C5-ACD3-909681B6E0AF.mp3" ></button>
     
     </li>
 		
 		            <li><b>拼    音：</b>èr  <button class="laba2"  role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/pth/C195DEDD-A529-4AC9-804F-BF89AE0C6198.mp3"></button></li>
 		
                    <li><b>字    义：</b>1.èr||no6 ①数目字：~个|两丈~尺。②两样：不要三心~意。☞[no6]的本字是“两”。 2.èr||ri6 序数：第~|~等货。</li>
                    
                </ul>
                </dd>
             </dl>
             <dl>
                <dt>
                  <p>阿</p>	
                </dt>
                <dd>

                <ul>
  	    
 		            <li><b>潮州音：</b>[a1 亚]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/A234E9BB-E62A-4E57-B5C8-270F81218E18.mp3" ></button>
     
     </li>
 		
 		            <li><b>潮州音：</b>[o1 窝]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/3DD9F61C-77D5-48F7-A404-584D475F86D5.mp3" ></button>
     
     </li>
 		
 		            <li><b>拼    音：</b>ā  <button class="laba2"  role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/pth/31502FCF-C7E9-4517-A7CD-E1F63165A0A5.mp3"></button></li>
 		
 		            <li><b>拼    音：</b>ē  <button class="laba2"  role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/pth/C9B771A8-896A-489C-A48C-4DB05B1B472E.mp3"></button></li>
 		
                    <li><b>字    义：</b>1.ā||a1 ①<方>词头，加在排行、小名或姓的前面：~大|~根|~王。②<方>加在某些亲尾称谓的前面：~妹|~姨|~公。③<潮>加在人名前面：~王菲|~山|~红。④音译用字：~门（基督教祈祷的结束语）|~拉伯人（分布于西亚、北非的一个民族）|~斯匹林（一种解热镇痛药）。⑤<潮>用在正反问句中表示选择，相当于普通话中的“还是”：是~（上不下是）[mi6]？|食茶~食咖啡？| 行路去~（是）坐船去？ 2.ē||o1 ①迎合，偏袒：~附|~其所好|~谀奉迎。②凹曲处：山~。</li>
                    
                </ul>
                </dd>
             </dl>
             <dl>
                <dt>
                  <p>殖</p>	
                </dt>
                <dd>

                <ul>
  	    
 		            <li><b>潮州音：</b>[sêg4 植]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/9C839EC2-02BE-4C34-A4E2-747DCBABA960.mp3" ></button>
     
     </li>
 		
 		            <li><b>汕头音：</b>[sig8 植]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/7EB4D1BC-5301-46B1-9603-3F8C10640F43.mp3" ></button>
     
     </li>
 		
 		            <li><b>澄海音：</b>[sig8 植]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/7EB4D1BC-5301-46B1-9603-3F8C10640F43.mp3" ></button>
     
     </li>
 		
 		            <li><b>潮州音：</b>[sig8 实]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/7EB4D1BC-5301-46B1-9603-3F8C10640F43.mp3" ></button>
     
     </li>
 		
 		            <li><b>揭阳音：</b>[sêg8 实]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/C0C08FEE-9533-4856-8250-A8CA3F2FB1E9.mp3" ></button>
     
     </li>
 		
 		            <li><b>拼    音：</b>zhí  <button class="laba2"  role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/pth/431928CF-90A6-45E0-882C-6CD9ED9C2469.mp3"></button></li>
 		
 		            <li><b>拼    音：</b>shi  <button class="laba2"  role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/pth/8BD1E7E6-F6F4-4DDF-A230-6A31E157EC50.mp3"></button></li>
 		
                    <li><b>字    义：</b>1.zhí||sêg4|汕澄sig8 生息，孳生：繁~。 2.shi||sig8|揭sêg8 尸骨：骨~。</li>
                    
                </ul>
                </dd>
             </dl>
             <dl>
                <dt>
                  <p>五</p>	
                </dt>
                <dd>

                <ul>
  	    
 		            <li><b>大写字：</b>伍</li>

 		            <li><b>潮州音：</b>[ngou6 午6]（白）
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/B5A82F8A-F587-4496-99FC-B3FD9437BEE0.mp3" ></button>
     
     </li>
 		
 		            <li><b>潮州音：</b>[ngou2 午]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/53888A1F-26D6-4920-A0E5-4DEE90A065DD.mp3" ></button>
     
     </li>
 		
 		            <li><b>潮州音：</b>[u2 宇]（文）
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/A47BBFF5-58FF-419D-98CF-54AF323A871C.mp3" ></button>
     
     </li>
 		
 		            <li><b>潮州音：</b>[u5 吾]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/A9906E46-BBD5-4052-91D5-DFA40E9DC11C.mp3" ></button>
     
     </li>
 		
 		            <li><b>拼    音：</b>wǔ  <button class="laba2"  role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/pth/04C38240-F81D-4617-9B39-16B7C8E651E8.mp3"></button></li>
 		
                    <li><b>字    义：</b>1.wǔ||ngou6 数目字，四加一的和：~人|~本书|~十~元。 2.wǔ||ngou2 义同“1”，多用于书面语：~岳|三皇~帝|三令~申|~谷不分。 3.wǔ||u2 义同“1”：二一添作~。 4.wǔ||u5 旧时乐谱记音符号的一个，相当于简谱的“6”。</li>
                    
                </ul>
                </dd>
             </dl>
             <dl>
                <dt>
                  <p>喔</p>	
                </dt>
                <dd>

                <ul>
  	    
 		            <li><b>潮州音：</b>[o1 窝]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/3DD9F61C-77D5-48F7-A404-584D475F86D5.mp3" ></button>
     
     </li>
 		
 		            <li><b>潮州音：</b>[og4 屋]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/C20C91BA-55AD-4131-9646-4E9CBE69933B.mp3" ></button>
     
     </li>
 		
 		            <li><b>拼    音：</b>ō  <button class="laba2"  role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/pth/A5594213-3D8D-485E-850E-5B372E671D68.mp3"></button></li>
 		
 		            <li><b>拼    音：</b>wō  <button class="laba2"  role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/pth/47829251-7BA5-49FC-A79C-6FD30F3DD34D.mp3"></button></li>
 		
                    <li><b>字    义：</b>1.ō||o1 叹词，表示了解：~，就是他！|~，我懂了。又表示惊异、痛苦：~哟，这么大的西瓜！|~哟，好痛！ 2.wō||og4 鸡叫声。</li>
                    
                </ul>
                </dd>
             </dl>''')
        self.assertEqual(parser.get_teochew_dict(), {
                        '贠': {'yuan2': 'uang5', 'yun4': 'ung7(姓)'}, 
                        '渐': {'jian4': 'ziam6', 'jian1': 'ziam1'}, 
                        '嗳': {'ai3': 'ai3|an6', 'ai4': 'ai7', 'ai1': 'ai1'}, 
                        '赚': {'zhuan4': 'tang3(俗)', 'zuan4': 'zuang3'}, 
                        '个': {'ge4': 'gai5|go6|gai7', 'ge3': 'gai5|gai7|go6'}, 
                        '二': {'er4': 'no6(训)|ri6'}, 
                        '阿': {'a1': 'a1', 'e1': 'o1'}, 
                        '殖': {'zhi2': 'sêg4|sig8', 'shi5': 'sig8'}, 
                        '五': {'wu3': 'ngou6(白)|ngou2|u2(文)|u5'}, 
                        '喔': {'o1': 'o1', 'wo1': 'og4'}
                        })

        parser = TeochewDictHTMLParser()
        parser.feed('''<dl>
                <dt>
                  <p>率</p>	
                </dt>
                <dd><ul>
  	    
 		            <li><b>潮州音：</b>[zug4 卒]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/19B9EEB1-A8A7-42E9-A264-8C2399C8B215.mp3" ></button>
     
     </li>
 		
 		            <li><b>潮州音：</b>[sug4 术4]（又）
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/4DE4130A-026D-474F-9CF7-BBA6F36F3600.mp3" ></button>
     
     </li>
 		
 		            <li><b>潮州音：</b>[lug8 律]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/141B509F-ECC5-4152-A017-C546F222DBA0.mp3" ></button>
     
     </li>
 		
 		            <li><b>拼    音：</b>shuài  <button class="laba2"  role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/pth/EFBC5258-F84D-4625-8CDF-1AA0B38CBF8A.mp3"></button></li>
 		
 		            <li><b>拼    音：</b>lǜ  <button class="laba2"  role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/pth/8E6C0FCE-18E5-4CA9-B925-81EE2FFCB881.mp3"></button></li>
 		
                    <li><b>字    义：</b>1.shuài||zug4|sug4 ①带领，统领：~队|~师。②轻易地，不细想、不慎重：轻~|草~。③爽直坦白：直~|坦~。④大率，大概，大略：~皆如此。⑤漂亮，俏皮：这字写得真~。也作“帅”。⑥遵循：~由旧章。⑦模范：一方表~。 2.lǜ||lug8 指两个相关的数在一定条件下的比值：速~|增长~|出勤~。</li>
                    
                </ul>
                </dd>
             </dl>
             <dl>
                <dt>
                  <p>汓</p>	
                </dt>
                <dd><ul>
  	    
 		            <li><b>潮州音：</b>[siu5 收5 ]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/C2EA48D3-31BE-49DE-8633-F86BD77C9182.mp3" ></button>
     
     </li>
 		
 		            <li><b>拼    音：</b>qiú  <button class="laba2"  role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/pth/8CF1326A-45F8-45D2-881E-A58493DC7353.mp3"></button></li>
 		
                    <li><b>字    义：</b>古同“泅”，游水。</li>
                    
                </ul>
                </dd>
             </dl>''')
        self.assertEqual(parser.get_teochew_dict(), {
            '率': {'shuai4': 'zug4|sug4(又)', 'lu:4': 'lug8'},
            '汓': {'qiu2': 'siu5'}
        })

if __name__ == '__main__':
    unittest.main()
