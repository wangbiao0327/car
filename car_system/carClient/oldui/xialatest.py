# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xialatest.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QVariant


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(384, 240)
        self.sheng_combox = QtWidgets.QComboBox(Dialog)
        self.sheng_combox.setGeometry(QtCore.QRect(50, 50, 60, 22))
        self.sheng_combox.setObjectName("sheng_combox")
        self.city_combox = QtWidgets.QComboBox(Dialog)
        self.city_combox.setGeometry(QtCore.QRect(180, 50, 60, 22))
        self.city_combox.setObjectName("city_combox")
        self.sheng_label = QtWidgets.QLabel(Dialog)
        self.sheng_label.setGeometry(QtCore.QRect(20, 120, 41, 9))
        self.sheng_label.setObjectName("sheng_label")
        self.city_label = QtWidgets.QLabel(Dialog)
        self.city_label.setGeometry(QtCore.QRect(180, 140, 41, 9))
        self.city_label.setObjectName("city_label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    # def retranslateUi(self, Dialog):
    #     _translate = QtCore.QCoreApplication.translate
    #     Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
    #     self.sheng_label.setText(_translate("Dialog", "TextLabel"))
    #     self.city_label.setText(_translate("Dialog", "TextLabel"))


    def retranslateUi(self, Dialog):
        dictPorovince = {2: u'北京', 3: u'安徽', 4: u'福建', 5: u'甘肃', 6: u'广东', 7: u'广西', 8: u'贵州', 9: u'海南',
                         10: u'河北',11: u'河南', 12: u'黑龙江',13: u'湖北', 14: u'湖南', 15: u'吉林', 16: u'江苏',
                     17: u'江西', 18: u'辽宁', 19: u'内蒙古', 20: u'宁夏',21: u'青海', 22: u'山东', 23: u'山西',
                     24: u'陕西',25: u'上海', 26: u'四川', 27: u'天津', 28: u'西藏', 29: u'新疆', 30: u'云南',
                     31: u'浙江', 32: u'重庆',33: u'香港', 34: u'澳门', 35: u'台湾'}

        self.dictCity = {2: {52: u'北京'}, 3: {36: u'安庆', 37: u'蚌埠', 38: u'巢湖', 39: u'池州', 40: u'滁州',
                                    41: u'阜阳', 42: u'淮北', 43: u'淮南', 44: u'黄山',
                                    45: u'六安', 46: u'马鞍山', 47: u'宿州', 48: u'铜陵', 49: u'芜湖', 50: u'宣城', 51: u'亳州',
                                    3401: u'合肥'},
                4: {53: u'福州', 54: u'龙岩', 55: u'南平',
                    56: u'宁德', 57: u'莆田', 58: u'泉州', 59: u'三明', 60: u'厦门', 61: u'漳州'}, 5: {62: u'兰州', 63: u'白银',
                                                                                           64: u'定西', 65: u'甘南',
                                                                                           66: u'嘉峪关',
                                                                                           67: u'金昌', 68: u'酒泉',
                                                                                           69: u'临夏', 70: u'陇南',
                                                                                           71: u'平凉', 72: u'庆阳',
                                                                                           73: u'天水', 74: u'武威',
                                                                                           75: u'张掖'},
                6: {76: u'广州', 77: u'深圳',
                    78: u'潮州', 79: u'东莞', 80: u'佛山', 81: u'河源', 82: u'惠州', 83: u'江门', 84: u'揭阳', 85: u'茂名',
                    86: u'梅州', 87: u'清远', 88: u'汕头',
                    89: u'汕尾', 90: u'韶关', 91: u'阳江', 92: u'云浮', 93: u'湛江', 94: u'肇庆', 95: u'中山', 96: u'珠海'},
                7: {97: u'南宁', 98: u'桂林', 99: u'百色',
                    100: u'北海', 101: u'崇左', 102: u'防城港', 103: u'贵港', 104: u'河池', 105: u'贺州', 106: u'来宾', 107: u'柳州',
                    108: u'钦州', 109: u'梧州',
                    110: u'玉林'},
                8: {111: u'贵阳', 112: u'安顺', 113: u'毕节', 114: u'六盘水', 115: u'黔东南', 116: u'黔南', 117: u'黔西南',
                    118: u'铜仁', 119: u'遵义'},
                9: {120: u'海口', 121: u'三亚', 122: u'白沙', 123: u'保亭', 124: u'昌江', 125: u'澄迈县', 126: u'定安县',
                    127: u'东方', 128: u'乐东', 129: u'临高县',
                    130: u'陵水', 131: u'琼海', 132: u'琼中', 133: u'屯昌县', 134: u'万宁', 135: u'文昌', 136: u'五指山',
                    137: u'儋州'}, 10: {138: u'石家庄', 139: u'保定',
                                      140: u'沧州', 141: u'承德', 142: u'邯郸', 143: u'衡水', 144: u'廊坊', 145: u'秦皇岛',
                                      146: u'唐山', 147: u'邢台', 148: u'张家口'}, 11: {149: u'郑州',
                                                                                 150: u'洛阳', 151: u'开封', 152: u'安阳',
                                                                                 153: u'鹤壁', 154: u'济源', 155: u'焦作',
                                                                                 156: u'南阳', 157: u'平顶山',
                                                                                 158: u'三门峡', 159: u'商丘',
                                                                                 160: u'新乡',
                                                                                 161: u'信阳', 162: u'许昌', 163: u'周口',
                                                                                 164: u'驻马店', 165: u'漯河',
                                                                                 166: u'濮阳'},
                12: {167: u'哈尔滨', 168: u'大庆', 169: u'大兴安岭', 170: u'鹤岗', 171: u'黑河',
                     172: u'鸡西', 173: u'佳木斯', 174: u'牡丹江', 175: u'七台河', 176: u'齐齐哈尔', 177: u'双鸭山', 178: u'绥化',
                     179: u'伊春'}, 13: {180: u'武汉', 181: u'仙桃', 182: u'鄂州',
                                       183: u'黄冈', 184: u'黄石', 185: u'荆门', 186: u'荆州', 187: u'潜江', 188: u'神农架林区',
                                       189: u'十堰', 190: u'随州', 191: u'天门', 192: u'咸宁', 193: u'襄樊', 194: u'孝感',
                                       195: u'宜昌', 196: u'恩施'},
                14: {197: u'长沙', 198: u'张家界', 199: u'常德', 200: u'郴州', 201: u'衡阳', 202: u'怀化', 203: u'娄底',
                     204: u'邵阳', 205: u'湘潭', 206: u'湘西',
                     207: u'益阳', 208: u'永州', 209: u'岳阳', 210: u'株洲'},
                15: {211: u'长春', 212: u'吉林', 213: u'白城', 214: u'白山', 215: u'辽源', 216: u'四平', 217: u'松原', 218: u'通化',
                     219: u'延边'},
                16: {220: u'南京', 221: u'苏州', 222: u'无锡', 223: u'常州', 224: u'淮安', 225: u'连云港', 226: u'南通',
                     227: u'宿迁', 228: u'泰州', 229: u'徐州', 230: u'盐城',
                     231: u'扬州', 232: u'镇江'},
                17: {233: u'南昌', 234: u'抚州', 235: u'赣州', 236: u'吉安', 237: u'景德镇', 238: u'九江', 239: u'萍乡',
                     240: u'上饶', 241: u'新余', 242: u'宜春',
                     243: u'鹰潭'},
                18: {244: u'沈阳', 245: u'大连', 246: u'鞍山', 247: u'本溪', 248: u'朝阳', 249: u'丹东', 250: u'抚顺', 251: u'阜新',
                     252: u'葫芦岛', 253: u'锦州', 254: u'辽阳',
                     255: u'盘锦', 256: u'铁岭', 257: u'营口'},
                19: {258: u'呼和浩特', 259: u'阿拉善盟', 260: u'巴彦淖尔盟', 261: u'包头', 262: u'赤峰', 263: u'鄂尔多斯', 264: u'呼伦贝尔',
                     265: u'通辽', 266: u'乌海', 267: u'乌兰察布市', 268: u'锡林郭勒盟', 269: u'兴安盟'},
                20: {270: u'银川', 271: u'固原', 272: u'石嘴山', 273: u'吴忠', 274: u'中卫'},
                21: {275: u'西宁', 276: u'果洛', 277: u'海北', 278: u'海东', 279: u'海南', 280: u'海西', 281: u'黄南',
                     282: u'玉树'}, 22: {283: u'济南', 284: u'青岛', 285: u'滨州',
                                       286: u'德州', 287: u'东营', 288: u'菏泽', 289: u'济宁', 290: u'莱芜', 291: u'聊城',
                                       292: u'临沂', 293: u'日照', 294: u'泰安', 295: u'威海', 296: u'潍坊', 297: u'烟台',
                                       298: u'枣庄', 299: u'淄博'},
                23: {300: u'太原', 301: u'长治', 302: u'大同', 303: u'晋城', 304: u'晋中', 305: u'临汾', 306: u'吕梁', 307: u'朔州',
                     308: u'忻州', 309: u'阳泉',
                     310: u'运城'},
                24: {311: u'西安', 312: u'安康', 313: u'宝鸡', 314: u'汉中', 315: u'商洛', 316: u'铜川', 317: u'渭南', 318: u'咸阳',
                     319: u'延安', 320: u'榆林'},
                25: {321: u'上海'},
                26: {322: u'成都', 323: u'绵阳', 324: u'阿坝', 325: u'巴中', 326: u'达州', 327: u'德阳', 328: u'甘孜', 329: u'广安',
                     330: u'广元', 331: u'乐山',
                     332: u'凉山', 333: u'眉山', 334: u'南充', 335: u'内江', 336: u'攀枝花', 337: u'遂宁', 338: u'雅安',
                     339: u'宜宾', 340: u'资阳', 341: u'自贡', 342: u'泸州'},
                27: {343: u'天津'},
                28: {344: u'拉萨', 345: u'阿里', 346: u'昌都', 347: u'林芝', 348: u'那曲', 349: u'日喀则', 350: u'山南'},
                29: {351: u'乌鲁木齐', 352: u'阿克苏',
                     353: u'阿拉尔', 354: u'巴音郭楞', 355: u'博尔塔拉', 356: u'昌吉', 357: u'哈密', 358: u'和田', 359: u'喀什',
                     360: u'克拉玛依', 361: u'克孜勒苏', 362: u'石河子',
                     363: u'图木舒克', 364: u'吐鲁番', 365: u'五家渠', 366: u'伊犁'},
                30: {367: u'昆明', 368: u'怒江', 369: u'普洱', 370: u'丽江', 371: u'保山', 372: u'楚雄', 373: u'大理',
                     374: u'德宏', 375: u'迪庆', 376: u'红河', 377: u'临沧', 378: u'曲靖', 379: u'文山', 380: u'西双版纳',
                     381: u'玉溪', 382: u'昭通'}, 31: {383: u'杭州', 384: u'湖州',
                                                   385: u'嘉兴', 386: u'金华', 387: u'丽水', 388: u'宁波', 389: u'绍兴',
                                                   390: u'台州', 391: u'温州', 392: u'舟山', 393: u'衢州'},
                32: {394: u'重庆'}, 33: {395: u'香港'},
                34: {396: u'澳门'}, 35: {397: u'台湾'}}

        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

        self.sheng_combox.setCurrentText(_translate("Dialog", "请选择"))
        for key,sheng in dictPorovince.items():
            self.sheng_combox.addItem(sheng, QVariant(key) )



        self.sheng_label.setText(_translate("Dialog", "省份："))
        self.city_label.setText(_translate("Dialog", "城市"))

        # QtGui.QWidget.connect(self.ui_sel.comboBox_province, QtCore.SIGNAL('activated(int)'), self.onActivated)
        self.sheng_combox.activated.connect(self.onActivated)

    def onActivated(self):
        cuindex = self.sheng_combox.currentIndex()
        for (keys, val) in self.dictCity[cuindex].items():
            self.ui_sel.comboBox_city.addItem(val, QVariant(keys))
