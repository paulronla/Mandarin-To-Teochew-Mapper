#coding=utf-8
import unittest
import json
from teochew_dict_htmlparser import Teochew_Dict_HTMLParser

class Test_Teochew_Dict_HTMLParser(unittest.TestCase):
    def test_getTeochewDict(self):
        parser = Teochew_Dict_HTMLParser()
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
        self.assertEqual(parser.getTeochewDict(),{'片': {'pian4': 'piang3|pin3(白)', 'pian1': 'piang3'}})
        parser = Teochew_Dict_HTMLParser()
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
        self.assertEqual(parser.getTeochewDict(),{'亡': {'wang2': 'bhuang5|mang5(汕)(又)', 'wu2': 'bho5'}})
        parser = Teochew_Dict_HTMLParser()
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
        self.assertEqual(parser.getTeochewDict(),{'张': {'zhang1': 'dion1(白)(姓)|ziang1(文)|dion3'}, '掀': {'xian1':'hiang1|hng1(又)|heng1(汕)(又)|hiaon1'}})
        parser = Teochew_Dict_HTMLParser()
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
        self.assertEqual(parser.getTeochewDict(),{'陂': {'bei1': 'bi1', 'pi2': 'pi5', 'po1': 'po1|bo1(汕)'}, '𫢗': {'': 'diang5'}, '仆': {'pu1': 'pog4', 'pu2': 'bog8'}, '鶪': {'ju2': 'gu6'}, '谁': {'shui2': 'sui5', 'shei2': 'sui5'}, '熟': {'shu2': 'sêg8', 'shou2': 'sêg8'}})

if __name__ == '__main__':
    unittest.main()
