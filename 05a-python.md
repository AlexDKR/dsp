# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Similarities:
>> They're both sequences.
>> 
>> Differences:
>> Tuples are immutable, while lists are mutable and you can modify order, placement, etc.
>> As a result, mapping, pushing, popping, concatenating, and more can be done with lists.
>> 
>> Tuples will work as keys in dictionaries. Technically, I'm assuming that they both would work.  
>> However, a property of tuples are that they are immutable. By definition and construction, they cannot be modified. This results in predictable and favorable behavior when working with dictionaries.
>> Lists, on the other hand are mutable and could result in unpredictable behavior.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Similarities:
>> They're both sequences.
>> 
>> Differences:
>> Lists are mutable allowing for methods like mapping, pushing, popping, concatenating, and more can be done with lists.
>> 
>> Sets can be faster in terms of performance when the sequences have lots of elements.
>> 
>> Lists are based on dynamic arrays and sets are based on hash tables.
>> Hash tables outperform dyanamic arrays when looking for an element when there are lots of elements
>> 
>> The following block of code shows an example of when removing elements from a set can be faster than removing elements from a list.

```python
import numpy as np
import time

# create a float list
float_list = [12.935566899972519, 1.2737220179218172, 5.9917727737389104, 12.198902112044435, 10.602724999696543, 5.0454097688086099, 3.8776725572805746, 13.097658945032524, 9.0898734692206506, 1.877757204612128, 0.86878303004599511, 4.4796525457125842, 9.9009228829070466, 11.15800530955412, 9.9474922550757565, 7.8634329150174596, 3.9851941728564699, 9.3055804026938969, 3.2850375211939169, 0.83936871663950408, 6.5917856421164807, 10.393063758451802, 6.5330268507627807, 1.6653933114204591, 10.758677334941837, 4.147039195929608, 3.1379028452991893, 6.5371820669798026, 12.195396343375895, 3.2315350267412968, 2.0576355931701302, 12.772488411930015, 3.9881325500232734, 12.845702546315337, 7.231758131454427, 11.158023418536601, 11.961710281360435, 11.504188028267521, 1.7415290726307875, 1.0380268593157695, 1.8186200009115525, 10.007248459865748, 0.53293013577232529, 10.981957539170747, 7.6897267481616893, 4.657205872086803, 9.4296229973583277, 9.5098038100107836, 13.065993305571673, 2.0810450652435337, 9.5446999427507819, 1.0083044393193206, 0.69311425193100007, 8.5137259558806022, 6.8545508872336702, 10.874534756768325, 1.125293359581403, 3.2764910957429993, 4.3324118293561868, 3.0611827618346652, 1.9551010568031204, 3.8873340373130989, 3.4132607359425151, 1.763570757943741, 12.292020117828601, 6.6758105396163545, 13.245504220438525, 4.6295045153290451, 1.7883625801070524, 11.379797484092109, 10.823166977069441, 8.3701513318620471, 11.528294062865619, 6.424545504936944, 2.2019122938768536, 12.172035704854805, 10.567223551867235, 10.047179688967901, 7.6336994648604453, 3.4272137930402438, 8.6196289515297231, 3.7490898607189411, 0.61664882093391216, 4.4794418479281646, 9.6008137946294436, 1.4291906730134003, 1.7324402852986964, 1.2197282853025668, 12.976245611408437, 7.2756241906060737, 2.4291007914061695, 10.161514581402949, 4.5267662978180736, 3.6587769970726103, 1.7644711359113332, 0.52562006869026878, 8.2279996212285553, 10.679258419039321, 5.6060942602499155, 10.521405732134959, 3.7174566516585958, 13.262216460131548, 10.662206328659071, 2.9278323923630367, 6.0266791345415029, 5.406708334349263, 3.1782022793368498, 12.001496433841544, 6.1263265735510082, 9.1727106514318244, 11.233134552638084, 10.637598505329438, 10.812729936136201, 9.1717153108055651, 8.8103393807363819, 7.1012672765798159, 4.3137936891951796, 0.91008654764785746, 11.584020200813082, 4.2211774266899038, 5.0148098310919158, 4.3782564895896083, 0.53692181842847764, 2.5812676085117374, 11.446166686987786, 7.5384784338763797, 5.3426611974417133, 7.0316508918736833, 8.3721706596693082, 5.832828967618048, 0.79002093036876886, 6.2927128121027822, 12.043602158406898, 1.3092368200441797, 9.3650511616548808, 10.398868128121805, 9.6457254214083257, 3.2307225268704247, 5.4258650688599861, 11.377776249191378, 2.5236636836281576, 8.0136419221841209, 1.6801450349931997, 9.9230746356110853, 10.163136647268898, 7.7153872159647507, 4.2702914563330161, 8.356381158689894, 5.8184893385038849, 12.593001926922186, 13.160084897176716, 11.032769031416432, 1.6925580989616464, 1.0461346913087581, 1.2813044260492332, 2.1845973164394139, 4.9047436867714485, 7.2145998383701953, 11.045770369908158, 3.7219406284192349, 2.4861703616907862, 6.449868468171764, 8.4333942626413823, 7.2943160654448338, 10.092755384289408, 8.8351856623402458, 9.6183670608221572, 1.4263132878066758, 2.4855264638943426, 0.82438242302687437, 11.897722759951293, 4.6267723136098624, 5.6868015975029698, 1.6579451704675108, 4.2545704754997882, 10.852545823797932, 1.286123655937945, 13.029834556362536, 10.890338046550923, 10.256394141790265, 5.8280575417494305, 5.4903790455350148, 2.8331026056885604, 5.2820214245922159, 8.3204839614048769, 10.264177429529717, 11.572459506312869, 7.8781089948589003, 2.8711479616742976, 2.7772291940542249, 0.92453068812985184, 1.8241849422397509, 11.20683919378655, 1.1008630942939448, 3.0176203693237698, 3.3253052444024847, 4.4908004614240262, 7.2454364525217914, 10.73528949137207, 8.2373356633099029, 6.3741889152403424, 7.5782884471418361, 7.4343508174078394, 11.191524690566698, 11.584704016465654, 5.1529162795629651, 10.727646001141432, 4.9751307469097901, 4.2138137515190284, 6.312425217756882, 11.26134122233394, 11.91544707403232, 1.705078844325489, 9.4239816820793259, 6.2111814219638575, 1.1798990073465419, 12.815498710741565, 4.955752731110465, 3.5115627848896001, 2.1515318992961738, 13.26978794770911, 3.1940988738981035, 1.6428819558231098, 5.064208766507309, 9.1759989339240065, 6.1529430997575973, 13.128541389265019, 12.013646642030158, 12.001872827563163, 11.279887862417356, 11.275532879843716, 11.464539462021149, 10.061759819133332, 3.0666701004095192, 4.9454006856931274, 8.8711093921000419, 11.270980269232496, 4.4591608633784219, 7.4684517127614676, 0.77457241293328716, 7.6800761509950348, 11.427150644678953, 10.398801138678813, 10.769992223873762, 7.6155891007699186, 11.025163204700988, 9.5305067947282431, 12.448402248287984, 7.5431102194474322, 3.9936655159744703, 9.405608510044166, 8.4391372209331568, 3.3202728258880514, 8.855472331631443, 1.2353105101124315, 12.113881836556336, 1.1451334606024588, 3.5530733065956115, 12.37448363605192, 10.025637633324413, 7.3862892125753312, 5.287234708324239, 2.2082008348708215, 5.3998616887730666, 10.590388919580279, 4.679635614688026, 7.8809843794140377, 8.3157945037569156, 10.162828195235141, 7.4588477529132993, 1.3715430437469265, 2.5664229181139233, 7.244456260829411, 10.110757486457505, 0.63464042578585378, 11.733287378951694, 9.9054060830021626, 4.335551010653516, 1.8500951666098162, 8.1462888481835876, 10.957555832073799, 1.7868648652235153, 8.9939049109031455, 3.3709217233384337, 12.363407246484591, 0.56993777864138484, 6.5595317498673609, 2.8310384756913507, 0.78447835323936199, 11.613355760075484, 8.9608159866006343, 2.9556392215748164, 10.351111650013992, 1.1776328551001853, 4.2594495784137738, 8.1649110221651249, 9.1507088050205034, 3.5988233772487521, 6.9333017214527857, 9.277288073204943, 0.7101963407118006, 6.5754082364348641, 8.7223501724375154, 10.729532229217696, 1.4149911783243638, 8.0653345072017402, 5.1848819870849985, 9.8993957406851614, 1.6842286397307049, 6.0655816086865562, 12.646394161572076, 2.9817011858809281, 12.787776880635983, 10.13607080695907, 2.5288099701804172, 9.9424652672784397, 1.5978809073990463, 9.4029955202750042, 5.5734397719433133, 9.4575629027291992, 13.163648108512412, 4.4186786654838173, 9.784332943962001, 4.2409995227915402, 4.7010896300313183, 2.3086506039738595, 10.688428468148944, 4.133966946249485, 10.192876989355579, 9.5844705824589393, 8.5736298398720869, 4.8702733192222469, 9.9922776472176356, 9.56700214048894, 2.7345852656508014, 5.8520591754180984, 12.103009809488611, 12.141894957763155, 6.909820632378544, 8.8484476110965513, 4.0755537624829294, 9.4246295755458132, 2.6109783484294611, 11.661895785531526, 5.6344277092250827, 7.6606613162762116, 8.5685368737344128, 3.3525634949809673, 3.1273953762758482, 7.5362528944792091, 6.3937409100069917, 6.1863302101371218, 4.6006743380554544, 7.3299600161431364, 3.4543728946366556, 5.5706542666318519, 10.289884997537285, 10.182933680994473, 10.661898820111677, 8.0375449410830022, 6.9713763176196979, 3.8074355259555319, 11.311715511389506, 0.66200112312349835, 1.3923237214308997, 12.630664783716149, 10.364243092353775, 13.246740720696829, 8.9190922441212468, 0.89560711752517363, 3.1737015483764921, 6.639774064117308, 4.5170270460451531, 4.0865400621750867, 7.4588787298872079, 2.772285181018205, 10.21353979224577, 2.370248334470193, 13.081319530203247, 9.8278556879765251, 10.586625079623589, 2.6159956549221905, 10.568467963652111, 5.7950524047558805, 0.91116473086676564, 5.3668541339075793, 8.1553812597348632, 6.2506134665015196, 4.7377191070488136, 12.935140998381726, 3.0096635211073393, 8.0608555792756391, 8.9798712365637687, 7.9139927498247431, 13.03411860108972, 2.8350293551124253, 12.719160328338889, 2.6866181256272115, 10.214706309480455, 4.4014235205338368, 5.4191823871703937, 2.0994679583449498, 8.6587137860843928, 7.3366775402458444, 8.5858933874613097, 12.442609083593076, 3.5471049475428362, 11.41632740450534, 10.811614604454668, 2.7944558506217092, 2.6766234775304087, 6.3510796585613107, 11.311239259994974, 9.02638735315203, 6.9726612743897327, 2.5507605550278414, 9.4433099918520718, 5.0741877720693438, 11.02351646414216, 6.0345626658443114, 5.97776642873949, 5.4016431754295589, 6.6976068151180117, 12.239978895310408, 9.9428226420400545, 10.722848036741732, 6.0796627112614336, 11.131722780672391, 0.6978919367473253, 4.2434146220233586, 8.6424006437463703, 3.888766462436418, 1.1737504473374201, 10.437808371538509, 2.9601869068470421, 2.9466449732173716, 7.7991526373383584, 6.6326421775018236, 12.870155103794243, 8.1008499134097196, 1.3726677289749376, 3.225399912618093, 10.306296670336527, 10.994099828105016, 11.69600978589644, 11.34461588469749, 1.6492035050807929, 5.2019513577924625, 12.007792759811041, 8.7963255815456165, 5.0522848207354114, 5.6683764230735818, 1.1899087639209727, 12.550388614496036, 13.107382352566212, 4.5513892630380823, 6.3647049039205372, 3.3829288129888653, 10.656196865424771, 10.208489639173408, 9.9485828588575522, 4.846975094499391, 6.3524876065463252, 5.806073255597024, 9.5963419480616849, 3.5237876727747364, 8.9431122119019442, 10.905238228569107, 8.1168986488342725, 5.3426404666244309, 3.2984826467359429, 4.3805145061040172, 6.5764924463374861, 9.5913423750001723, 11.858723689317999, 4.866827579255907, 8.3381447993991067, 10.675185095444625, 6.8069839991821572, 6.1719108409541796, 10.820798598131619, 6.0959322058224501, 6.9300136224520701, 2.4281604241509616, 11.582130453794965, 10.421308979581688, 9.8422881807682696, 5.2355522933417564, 10.654279260844296, 11.183955885680877, 7.4385368798090328, 10.117700945443481, 3.4473655473707936, 12.941075846026528, 3.8782386041595518, 7.4605130482178588, 11.975748696907289, 8.5192693025790973, 4.8358071804452978, 8.627920968766178, 0.74923692605270986, 1.1090679530858312, 11.387357012138176, 4.105939800295678, 11.851616361439669, 9.4656414899354644, 10.640326924603952, 5.7894152792770317, 2.8270854952197979, 12.545267262366762, 9.4303401367677306, 7.1079318943262315, 11.312736055514662, 5.4402498085547863, 10.610511244530947, 0.62049708105861323, 10.287579240674971, 7.7369961564611955, 8.5582414066131332, 9.2811658233211922, 5.7011827209984238, 6.7887781580070801, 3.8696643339212571, 7.445199822042591, 5.7698540794511848, 4.9724410110755519, 6.5654562814341748, 12.285768074258556, 5.6775553538703596, 6.8099686193992888, 10.255730500991065, 6.3103633231334104, 11.106952528898475, 7.6910245403288968, 5.4409982669316719, 1.657694971188731, 1.6586560335920524, 2.8239853518760643, 2.7898093122007253, 6.7902289409766512, 5.495709384851593, 10.917064441794054, 5.3087264200163036, 4.8308708216469709, 5.7846412414241701, 0.92032731748305285, 13.054541527738962, 6.4901288079076824, 13.283000504092653, 5.9502136885695975, 10.082895980309958, 5.9426333719604658, 8.1797740012567779, 9.3283633969180073, 0.62824721798056371, 9.3283862001840419, 0.8449148379719631, 2.916018640946584, 5.6105439351591446, 3.4243102040847377, 7.6680349042146707, 0.51328389261637997, 6.7532959330986362, 4.2580819114067996, 6.7691173465015382, 12.499547513323627, 6.1663927571612085, 3.5192345028908534, 2.414919835937765, 1.9691712393278025, 6.7348810401484123, 6.4017503712479993, 8.3089989117284411, 12.680078628321029, 3.0501170376868703, 5.8762022284570152, 5.0689414189717068, 2.4925411582117452, 11.429906735619843, 4.8000967658555638, 11.881112294480367, 13.138287614973258, 1.1422787975913891, 8.8077271160258714, 7.8589376830665492, 11.182612776150519, 3.4645846695168814, 12.067561972764718, 8.6505489848771866, 3.1562895758290552, 1.102154019617926, 8.9382462890527439, 5.3243097342318864, 3.2295860303415966, 9.2301338927475332, 10.583370859854183, 8.1216818907618276, 9.7680489622195878, 2.3937712791652901, 3.2048496462941602, 12.090951818922157, 6.7151941711703831, 0.74119737392911555, 11.637585127783799, 9.9726818875301273, 5.7708367216287249, 4.1979605733135283, 1.5594782210572162, 7.6376743122004989, 3.8291920631966621, 10.120812231953474, 6.3468000344017454, 7.2848899791375166, 7.8567085115915765, 12.320016600153291, 7.1157880190066951, 5.180971955390091, 6.4385518037881191, 1.8273294397103443, 11.409780184058162, 0.63154191840283713, 0.94032116841837454, 4.3744725573554124, 6.7705393096858977, 5.9549315246361489, 7.2435538817625051, 0.85870293301406664, 12.485049272364945, 3.0263863670777882, 9.4014010732338864, 10.287258333342907, 10.715826495017165, 12.186222367943197, 11.374339723793961, 6.4646694083039016, 11.301620964447221, 9.0824229216277086, 11.623373362480283, 11.025927852013524, 10.724225617177442, 6.3271990634471722, 8.6015786857773282, 11.203596854572792, 4.1723977845713138, 3.0135894561367622, 6.3199825135194052, 12.775527261974547, 12.612453136879495, 12.449587377274028, 6.9918528592945641, 3.2818953746739044, 8.8350179799676773, 5.8269068860504163, 4.2906785134845666, 4.859481828660587, 9.2006441430459898, 10.575644933548432, 13.089293633064949, 3.5050728728914309, 10.368131103918682, 9.1477123074892042, 6.3867251982893514, 10.146300393126211, 10.726843438650247, 5.0603395326157967, 1.4377787859528284, 5.4347846704334586, 8.5562295505854244, 6.4837361627652319, 9.1501113264753098, 6.0644300953389596, 9.8746872811612132, 3.13011168982207, 6.4313139969699797, 12.325769472451853, 11.065298266203355, 12.84368820674014, 4.8458471192337402, 4.1274678631888602, 3.0356889515980798, 3.6633146120394771, 4.6551999874304189, 11.810541964744559, 11.920099022596752, 4.1445548451950049, 8.7344731945091905, 8.6312787362809846, 7.2349874893872048, 10.939732023201737, 1.3737334482407335, 11.634516813633418, 4.9059954770598511, 3.0454928012988591, 12.693955812450703, 4.0417401553334855, 10.15725822493026, 3.7156033532782278, 1.9723728604939155, 5.3227175457713081, 1.2387093759648977, 6.7360221588924905, 12.731352072089351, 9.7544659520913797, 11.648629107442279, 4.4214029539240283, 3.6007948439752, 3.3525492235393148, 12.857161299822648, 9.7133044599662597, 6.4719377152053204, 4.5107730637565426, 7.1441501178242994, 9.0353746340155698, 3.7167499821729297, 0.8313387036638944, 3.673060679128608, 2.5701339122783735, 4.9528116666212725, 8.8105467412348411, 9.7169412494114678, 9.731098832095018, 9.7052196092415297, 7.5860597661454454, 8.9429364851324582, 10.827204555645681, 5.5225642441690042, 12.231351999614763, 7.7342325339356552, 12.234924663480525, 10.299612407297396, 5.9448290656117582, 7.3779092740477115, 6.2819126061711348, 3.3378781204214847, 9.0883934871828149, 1.7950002727277878, 2.8514975858580942, 6.0096683259762642, 13.0373074696994, 0.51155997664434949, 5.215852602999532, 9.0748742594572374, 4.1427219601282461, 5.4562889324230914, 2.8943359138061924, 12.85243900256541, 6.8030685227333478, 12.890809316134721, 12.351301229282068, 12.13423110995398, 10.411514359648717, 2.2481570628322158, 11.873933111532425, 3.68830443928388, 5.6288077946344632, 1.9963937414322872, 4.6277981033410951, 3.9334354656314803, 4.4709479097345808, 1.6421768561457868, 7.1368348482782338, 3.9900718497479377, 12.929660812511912, 5.9008922591029576, 2.4904136107403092, 13.251105684016274, 2.7247919287138758, 2.1837475062774647, 3.2915612168407593, 11.884261609639267, 7.350166958200667, 8.5617209934410479, 8.2733766966289313, 10.499452339836743, 5.5905284057742168, 6.0192370569427887, 10.441159899710472, 10.304420889409679, 4.0925442330909014, 10.900084032093337, 6.0898889677783039, 6.783242575978, 6.3060329761263247, 1.2960327069258355, 3.0258932669221412, 4.4962077439842361, 8.0404172917405496, 4.8785793151644272, 12.488766020143615, 2.416094962526627, 9.1835720663653149, 10.060676385276647, 10.054853359234825, 1.5200945211436292, 5.0832372229388012, 8.6311596093754641, 10.796475402060969, 1.4589585894396593, 9.5202290428938898, 1.9771114042248314, 4.5813498209875947, 4.8280522667108219, 12.52220270643458, 6.3942443492415224, 1.7857711504555511, 4.9714618039327805, 12.324453425221598, 9.8512961309392342, 7.7724375094351021, 12.435530956605557, 7.1001939396722014, 5.6982869457418595, 9.7523369777903088, 6.3916182110434692, 1.5475439904930439, 6.1202602994018909, 4.8582423727455053, 1.4387877867412739, 11.397343677677043, 1.9462021242379792, 5.1134941889909573, 11.518241546739718, 3.3087204780754988, 10.488815855048777, 8.9665180151031674, 4.5392522491437992, 12.834686578828943, 12.897721625493565, 2.625972183525771, 11.804176835674713, 2.2532538383971001, 11.38679193750901, 9.0931127139452048, 11.219751040220757, 8.8189361935935526, 0.85605819538644712, 3.2833541182510744, 12.598899770640157, 7.1393065647083551, 4.4906889631686315, 11.825902591771936, 5.7601162023143644, 5.053958007181854, 5.7753067196844512, 8.0094614858476483, 4.8157861959364086, 3.6661799033195042, 5.4415806544948939, 12.658156464655304, 8.9583815374298386, 1.1162751852871438, 12.561213638985855, 6.3436190899948093, 1.5021275660209057, 12.621077555059573, 5.0197498315802846, 2.156175866169403, 7.7476658814262711, 13.138196296317762, 13.192020383037056, 4.8567894131193858, 3.819680781626869, 10.877320952450267, 2.4549911967168883, 8.3287472043970503, 7.49950673689764, 7.2330770216121669, 1.8933383254420832, 9.7845002024974121, 0.56964764112791078, 10.448071310131139, 11.727453106193908, 1.2725963906958626, 4.8924603658208738, 7.5963051079396351, 3.7722615688573189, 10.314086111003327, 6.0683489883467381, 11.977157242775753, 6.1286150741450811, 8.5483474389014553, 11.839251948601454, 5.8034554773703881, 10.057647589908177, 6.2602506750831211, 2.3175985764690807, 12.479012930445107, 5.5003540976994021, 4.8428530492375614, 1.614162789257938, 10.172177208912212, 5.9608579426117529, 1.0489056016213951, 7.0410485702583534, 10.25696886300376, 6.824090471009832, 7.1493208045586947, 12.388780438706455, 4.892829690658604, 3.931705781433108, 8.9863130152987303, 7.6562843917883887, 5.5195464860754697, 4.5121986853129119, 7.7565341796769038, 2.3585564967742227, 6.786760006178298, 1.7243867798451662, 8.9337241718325444, 8.7503012534840181, 9.9967819906887403, 1.5058097987757095, 7.1733956900640301, 10.286124111328357, 2.5220988516673102, 5.8605393508149977, 8.4833289808340702, 2.0231543039014852, 4.6212331364230526, 11.280349675034747, 2.1218885440688142, 7.5455832903829547, 10.430974213710272, 2.1439709086855272, 4.037276549870219, 2.396066491302359, 5.2819615424533097, 8.6139621363776389, 8.5156025520766132, 6.0294668404992651, 9.3676979323657488, 3.8042023210508122, 10.880535262221855, 4.0759659296859798, 5.5874109506518268, 5.0288556974598846, 4.1573515821634404, 2.3841897757171706, 10.154648522703098, 11.733324847880418, 8.2862767164010425, 6.4287542990626605, 2.2303067706428141, 2.5418814304376598, 8.2583917187628373, 3.6920278233692603, 5.0971590244415452, 7.5557296094669599, 5.9085683315116233, 2.7364702154816358, 1.5897061288483429, 9.428411079953321, 3.6849345097944695, 1.9725696420940437, 1.6892321365464695, 7.7160813317895647, 3.4227486997747363, 0.67090974999880471, 5.0810891343922142, 0.66823738607639882, 7.1378355304311931, 1.1146269086337215, 9.9661258749345976, 2.392449061792381, 10.311650318819206, 5.6853895311658382, 3.3835569253042297, 5.6230256734069073, 10.419865375517769, 12.897162401166463, 11.04992240038435, 2.1147422253048038, 2.7597491633165747, 13.192767042844807, 3.1075728026933036, 9.4852374429906874, 10.50163236819683, 6.6599815023221955, 6.0236695644840639, 12.073109422390271, 12.010596233616084, 11.122198774826337, 12.232402374287677, 8.2358804429325509, 10.375649645772684, 9.6238891228918515, 4.0361692782479448, 8.8179658698152021, 7.7238031214798584, 5.7226176724993438, 10.812304680629369, 10.205206004619175, 12.495617609988066, 3.4828112016797479, 0.90022196401819765, 9.032163641884484, 6.6183117563543634, 6.9660341496419207, 4.1536434940222104, 12.032455726733932]

# create a list of elements and a known value
element_list = range(0,1000,100)
gibberish_element = 10328210.1249031

# insert the known value into the float_list
for index in element_list: float_list.insert(index, gibberish_element)

# create a float set
float_set = set(float_list)


# remove the known element from the float list
list_time_0 = time.time()
while gibberish_element in float_list:
    float_list.remove(gibberish_element)
list_time_1 = time.time()

# calculate the time it takes to remove the known element from a list
list_removal_time = list_time_1 - list_time_0


# remove the known elemnt from the float set
set_time_0 = time.time()
float_set.remove(gibberish_element)
set_time_1 = time.time()

# calculate the time it takes to remove the known element from a set
set_removal_time = set_time_1 - set_time_0

# print out the performance results
print 'Given: The list and sets are identical and are ~1000 elements.'
print '       There are about 10 of the known element in each.'
print
print 'list element removal time: %5.1fus.' % (list_removal_time * 10**6)
print 'set element removal time : %5.1fus.' % (set_removal_time * 10**6)
print
```
>> The following shows the results of the previous block of code:
>>    

```
Given: The list and sets are identical and are ~1000 elements.
       There are about 10 of the known element in each.

list element removal time: 182.2us.
set element removal time :   1.0us.
```

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Python's 'lambda' is an operator used to create assignments that behave like functions.
>> 
>> It is used for one-time use, terse functions and complete expressions without creating multiple lines in a method, further away from the executed statement.
>>  
>> The code block below creates a list of keys from a dictionary. The sorted function is used to sort the list of names by the last name. This is achieved by the 'key' argument and with a lambda function.

```python
# Q3 Lambda functions
# pull in the faculty dictionary from the advanced file
faculty_dict = {('Yimei', 'Li'): [' Ph.D.', 'Assistant Professor of Biostatistics', 'liy3@email.chop.edu'], ('Hongzhe', 'Li'): [' Ph.D', 'Professor of Biostatistics', 'hongzhe@upenn.edu'], ('Justine', 'Shults'): [' Ph.D.', 'Professor of Biostatistics', 'jshults@mail.med.upenn.edu'], ('Wei', 'Yang'): [' Ph.D.', 'Assistant Professor of Biostatistics', 'weiyang@mail.med.upenn.edu'], ('Matthew', 'Bryan'): [' PhD', 'Assistant Professor of Biostatistics', 'bryanma@upenn.edu'], ('Kathleen', 'Propert'): [' Sc.D.', 'Professor of Biostatistics', 'propert@mail.med.upenn.edu'], ('Wensheng', 'Guo'): [' Ph.D', 'Professor of Biostatistics', 'wguo@mail.med.upenn.edu'], ('Phyllis', 'Gimotty'): [' Ph.D', 'Professor of Biostatistics', 'pgimotty@upenn.edu'], ('Jonas', 'Ellenberg'): [' Ph.D.', 'Professor of Biostatistics', 'jellenbe@mail.med.upenn.edu'], ('Wei-Ting', 'Hwang'): [' Ph.D.', 'Associate Professor of Biostatistics', 'whwang@mail.med.upenn.edu'], ('Michelle', 'Ross'): [' PhD', 'Assistant Professor is Biostatistics', 'michross@upenn.edu'], ('Jinbo', 'Chen'): [' Ph.D.', 'Associate Professor of Biostatistics', 'jinboche@upenn.edu'], ('Sharon', 'Xie'): [' Ph.D.', 'Associate Professor of Biostatistics', 'sxie@mail.med.upenn.edu'], ('Jason', 'Roy'): [' Ph.D.', 'Associate Professor of Biostatistics', 'jaroy@mail.med.upenn.edu'], ('Mingyao', 'Li'): [' Ph.D.', 'Associate Professor of Biostatistics', 'mingyao@mail.med.upenn.edu'], ('Yenchih', 'Hsu'): [' Ph.D.', 'Assistant Professor of Biostatistics', 'hsu9@mail.med.upenn.edu'], ('Mary', 'Sammel'): [' Sc.D.', 'Professor of Biostatistics', 'msammel@cceb.med.upenn.edu'], ('Warren', 'Bilker'): ['Ph.D.', 'Professor of Biostatistics', 'warren@upenn.edu'], ('A.', 'Localio'): [' JD MA MPH MS PhD', 'Associate Professor of Biostatistics', 'rlocalio@upenn.edu'], ('Haochang', 'Shou'): [' Ph.D.', 'Assistant Professor of Biostatistics', 'hshou@mail.med.upenn.edu'], ('Rui', 'Xiao'): [' PhD', 'Assistant Professor of Biostatistics', 'rxiao@mail.med.upenn.edu'], ('Benjamin', 'French'): [' PhD', 'Associate Professor of Biostatistics', 'bcfrench@mail.med.upenn.edu'], ('Sarah', 'Ratcliffe'): [' Ph.D.', 'Associate Professor of Biostatistics', 'sratclif@upenn.edu'], ('Rui', 'Feng'): [' Ph.D', 'Assistant Professor of Biostatistics', 'ruifeng@upenn.edu'], ('Dawei', 'Xie'): [' PhD', 'Assistant Professor of Biostatistics', 'dxie@upenn.edu'], ('Pamela', 'Shaw'): [' PhD', 'Assistant Professor of Biostatistics', 'shawp@upenn.edu'], ('Nandita', 'Mitra'): [' Ph.D.', 'Associate Professor of Biostatistics', 'nanditam@mail.med.upenn.edu'], ('Scarlett', 'Bellamy'): [' Sc.D.', 'Associate Professor of Biostatistics', 'bellamys@mail.med.upenn.edu'], ('Marshall', 'Joffe'): [' MD MPH Ph.D', 'Professor of Biostatistics', 'mjoffe@mail.med.upenn.edu'], ('Susan', 'Ellenberg'): [' Ph.D.', 'Professor of Biostatistics', 'sellenbe@upenn.edu'], ('Knashawn', 'Morales'): [' Sc.D.', 'Associate Professor of Biostatistics', 'knashawn@mail.med.upenn.edu'], ('Alisa', 'Stephens'): [' Ph.D.', 'Assistant Professor of Biostatistics', 'alisaste@mail.med.upenn.edu'], ('Rebecca', 'Hubbard'): [' PhD', 'Associate Professor of Biostatistics', 'rhubb@mail.med.upenn.edu'], ('Mary', 'Putt'): [' PhD ScD', 'Professor of Biostatistics', 'mputt@mail.med.upenn.edu'], ('Andrea', 'Troxel'): [' ScD', 'Professor of Biostatistics', 'atroxel@mail.med.upenn.edu'], ('Russell', 'Shinohara'): ['0', 'Assistant Professor of Biostatistics', 'rshi@mail.med.upenn.edu'], ('J.', 'Landis'): [' B.S.Ed. M.S. Ph.D.', 'Professor of Biostatistics', 'jrlandis@mail.med.upenn.edu']}

# create a unique list of names from the dictionary
last_name_list = []
for name in faculty_dict.keys(): 
    if name[1] not in last_name_list:
        last_name_list.append(name[1])

print 'Last Name List:'
print last_name_list[:4]
print

# sort the last name list by last name
last_name_list = sorted(last_name_list, key=lambda name:name[0])

print 'Sorted Last Name List:'
print last_name_list[:4]
print
```
>> The output of the code given above is shown below:
>>    

```
Last Name List:
['Ellenberg', 'Li', 'Xiao', 'Shults']

Sorted Last Name List:
['Bryan', 'Bellamy', 'Bilker', 'Chen']  
```


---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are a way to manipulate a list in a single line, as opposed to coding a loop with multiple lines.  
>>  
>> The code below takes the keys of the faculty dictionary we've been using, and creates a name list.  
>> A list comprehension and map are used to create a list of first names only. The map command allows less typing and achieves the same result.  
>> The filter command is used to qualify and items in a list, which is beyond the capability of map.  
>>  
>> Set comprehensions and dictionary comprehensions are thrown in as well.  

```python
# Q4 list, set, and dictionary comprehensions
#    map and filter

# pull in the faculty dictionary from the advanced file
faculty_dict = {('Yimei', 'Li'): [' Ph.D.', 'Assistant Professor of Biostatistics', 'liy3@email.chop.edu'], ('Hongzhe', 'Li'): [' Ph.D', 'Professor of Biostatistics', 'hongzhe@upenn.edu'], ('Justine', 'Shults'): [' Ph.D.', 'Professor of Biostatistics', 'jshults@mail.med.upenn.edu'], ('Wei', 'Yang'): [' Ph.D.', 'Assistant Professor of Biostatistics', 'weiyang@mail.med.upenn.edu'], ('Matthew', 'Bryan'): [' PhD', 'Assistant Professor of Biostatistics', 'bryanma@upenn.edu'], ('Kathleen', 'Propert'): [' Sc.D.', 'Professor of Biostatistics', 'propert@mail.med.upenn.edu'], ('Wensheng', 'Guo'): [' Ph.D', 'Professor of Biostatistics', 'wguo@mail.med.upenn.edu'], ('Phyllis', 'Gimotty'): [' Ph.D', 'Professor of Biostatistics', 'pgimotty@upenn.edu'], ('Jonas', 'Ellenberg'): [' Ph.D.', 'Professor of Biostatistics', 'jellenbe@mail.med.upenn.edu'], ('Wei-Ting', 'Hwang'): [' Ph.D.', 'Associate Professor of Biostatistics', 'whwang@mail.med.upenn.edu'], ('Michelle', 'Ross'): [' PhD', 'Assistant Professor is Biostatistics', 'michross@upenn.edu'], ('Jinbo', 'Chen'): [' Ph.D.', 'Associate Professor of Biostatistics', 'jinboche@upenn.edu'], ('Sharon', 'Xie'): [' Ph.D.', 'Associate Professor of Biostatistics', 'sxie@mail.med.upenn.edu'], ('Jason', 'Roy'): [' Ph.D.', 'Associate Professor of Biostatistics', 'jaroy@mail.med.upenn.edu'], ('Mingyao', 'Li'): [' Ph.D.', 'Associate Professor of Biostatistics', 'mingyao@mail.med.upenn.edu'], ('Yenchih', 'Hsu'): [' Ph.D.', 'Assistant Professor of Biostatistics', 'hsu9@mail.med.upenn.edu'], ('Mary', 'Sammel'): [' Sc.D.', 'Professor of Biostatistics', 'msammel@cceb.med.upenn.edu'], ('Warren', 'Bilker'): ['Ph.D.', 'Professor of Biostatistics', 'warren@upenn.edu'], ('A.', 'Localio'): [' JD MA MPH MS PhD', 'Associate Professor of Biostatistics', 'rlocalio@upenn.edu'], ('Haochang', 'Shou'): [' Ph.D.', 'Assistant Professor of Biostatistics', 'hshou@mail.med.upenn.edu'], ('Rui', 'Xiao'): [' PhD', 'Assistant Professor of Biostatistics', 'rxiao@mail.med.upenn.edu'], ('Benjamin', 'French'): [' PhD', 'Associate Professor of Biostatistics', 'bcfrench@mail.med.upenn.edu'], ('Sarah', 'Ratcliffe'): [' Ph.D.', 'Associate Professor of Biostatistics', 'sratclif@upenn.edu'], ('Rui', 'Feng'): [' Ph.D', 'Assistant Professor of Biostatistics', 'ruifeng@upenn.edu'], ('Dawei', 'Xie'): [' PhD', 'Assistant Professor of Biostatistics', 'dxie@upenn.edu'], ('Pamela', 'Shaw'): [' PhD', 'Assistant Professor of Biostatistics', 'shawp@upenn.edu'], ('Nandita', 'Mitra'): [' Ph.D.', 'Associate Professor of Biostatistics', 'nanditam@mail.med.upenn.edu'], ('Scarlett', 'Bellamy'): [' Sc.D.', 'Associate Professor of Biostatistics', 'bellamys@mail.med.upenn.edu'], ('Marshall', 'Joffe'): [' MD MPH Ph.D', 'Professor of Biostatistics', 'mjoffe@mail.med.upenn.edu'], ('Susan', 'Ellenberg'): [' Ph.D.', 'Professor of Biostatistics', 'sellenbe@upenn.edu'], ('Knashawn', 'Morales'): [' Sc.D.', 'Associate Professor of Biostatistics', 'knashawn@mail.med.upenn.edu'], ('Alisa', 'Stephens'): [' Ph.D.', 'Assistant Professor of Biostatistics', 'alisaste@mail.med.upenn.edu'], ('Rebecca', 'Hubbard'): [' PhD', 'Associate Professor of Biostatistics', 'rhubb@mail.med.upenn.edu'], ('Mary', 'Putt'): [' PhD ScD', 'Professor of Biostatistics', 'mputt@mail.med.upenn.edu'], ('Andrea', 'Troxel'): [' ScD', 'Professor of Biostatistics', 'atroxel@mail.med.upenn.edu'], ('Russell', 'Shinohara'): ['0', 'Assistant Professor of Biostatistics', 'rshi@mail.med.upenn.edu'], ('J.', 'Landis'): [' B.S.Ed. M.S. Ph.D.', 'Professor of Biostatistics', 'jrlandis@mail.med.upenn.edu']}

name_list = sorted(faculty_dict.keys())
# list comprehension example:
# get the last names only from last_name_list
print 'original name_list:'
print name_list
print

# list comprehension of name_list
first_name_list = [name[0] for name in name_list]
print 'first-name results of list comprehension of name_list'
print first_name_list
print



# map example 
# creating a new list based on map
mapped_first_name_list = map(lambda name: name[0], name_list)
print 'first-name results using map and name_list'
print mapped_first_name_list
print



# filter example
# filtering out the first names that begin with s
print 'first name list that begins with s using filter and name_list'
first_name_s_list = filter(lambda name: name[0].lower()[0] == 's', name_list)
print first_name_s_list
print
print
print



# set comprehension
name_set = set(name_list)
first_name_set = {name[0] for name in name_set}
print 'first name set using a set comprehension'
print first_name_set
print
print
print



# dictionary comprehension
faculty_first_name_dict = {name[0]: credentials for name, credentials in faculty_dict.items()}

print 'original dictionary:'
for key, value in faculty_dict.iteritems():
    print '%26s: %s' % (key, value)
print
print 'dictionary comprehension used to provide first name as key'
for key, value in faculty_first_name_dict.iteritems():
    print '%10s: %s' % (key, value)
```

>> Output of the above is shown below:  
>> 

```
original name_list:
[('A.', 'Localio'), ('Alisa', 'Stephens'), ('Andrea', 'Troxel'), ('Benjamin', 'French'), ('Dawei', 'Xie'), ('Haochang', 'Shou'), ('Hongzhe', 'Li'), ('J.', 'Landis'), ('Jason', 'Roy'), ('Jinbo', 'Chen'), ('Jonas', 'Ellenberg'), ('Justine', 'Shults'), ('Kathleen', 'Propert'), ('Knashawn', 'Morales'), ('Marshall', 'Joffe'), ('Mary', 'Putt'), ('Mary', 'Sammel'), ('Matthew', 'Bryan'), ('Michelle', 'Ross'), ('Mingyao', 'Li'), ('Nandita', 'Mitra'), ('Pamela', 'Shaw'), ('Phyllis', 'Gimotty'), ('Rebecca', 'Hubbard'), ('Rui', 'Feng'), ('Rui', 'Xiao'), ('Russell', 'Shinohara'), ('Sarah', 'Ratcliffe'), ('Scarlett', 'Bellamy'), ('Sharon', 'Xie'), ('Susan', 'Ellenberg'), ('Warren', 'Bilker'), ('Wei', 'Yang'), ('Wei-Ting', 'Hwang'), ('Wensheng', 'Guo'), ('Yenchih', 'Hsu'), ('Yimei', 'Li')]  

first-name results of list comprehension of name_list  
['A.', 'Alisa', 'Andrea', 'Benjamin', 'Dawei', 'Haochang', 'Hongzhe', 'J.', 'Jason', 'Jinbo', 'Jonas', 'Justine', 'Kathleen', 'Knashawn', 'Marshall', 'Mary', 'Mary', 'Matthew', 'Michelle', 'Mingyao', 'Nandita', 'Pamela', 'Phyllis', 'Rebecca', 'Rui', 'Rui', 'Russell', 'Sarah', 'Scarlett', 'Sharon', 'Susan', 'Warren', 'Wei', 'Wei-Ting', 'Wensheng', 'Yenchih', 'Yimei']  
    
first-name results using map and name_list  
['A.', 'Alisa', 'Andrea', 'Benjamin', 'Dawei', 'Haochang', 'Hongzhe', 'J.', 'Jason', 'Jinbo', 'Jonas', 'Justine', 'Kathleen', 'Knashawn', 'Marshall', 'Mary', 'Mary', 'Matthew', 'Michelle', 'Mingyao', 'Nandita', 'Pamela', 'Phyllis', 'Rebecca', 'Rui', 'Rui', 'Russell', 'Sarah', 'Scarlett', 'Sharon', 'Susan', 'Warren', 'Wei', 'Wei-Ting', 'Wensheng', 'Yenchih', 'Yimei']  
  
first name list that begins with s using filter and name_list  
[('Sarah', 'Ratcliffe'), ('Scarlett', 'Bellamy'), ('Sharon', 'Xie'), ('Susan', 'Ellenberg')]  
  
  
  
first name set using a set comprehension  
set(['Sarah', 'Sharon', 'Russell', 'Kathleen', 'Wei', 'Matthew', 'Hongzhe', 'Pamela', 'Mary', 'Scarlett', 'Benjamin', 'Jinbo', 'Wensheng', 'A.', 'Mingyao', 'Jonas', 'Alisa', 'Phyllis', 'Andrea', 'Rebecca', 'Nandita', 'Michelle', 'Wei-Ting', 'Susan', 'Rui', 'Yenchih', 'Yimei', 'Jason', 'Knashawn', 'Marshall', 'Justine', 'Haochang', 'J.', 'Dawei', 'Warren'])  
   
  
  
original dictionary:  
    ('Susan', 'Ellenberg'): [' Ph.D.', 'Professor of Biostatistics', 'sellenbe@upenn.edu']  
           ('Yimei', 'Li'): [' Ph.D.', 'Assistant Professor of Biostatistics', 'liy3@email.chop.edu']  
           ('Rui', 'Xiao'): [' PhD', 'Assistant Professor of Biostatistics', 'rxiao@mail.med.upenn.edu']  
         ('Hongzhe', 'Li'): [' Ph.D', 'Professor of Biostatistics', 'hongzhe@upenn.edu']  
     ('Justine', 'Shults'): [' Ph.D.', 'Professor of Biostatistics', 'jshults@mail.med.upenn.edu']  
    ('Sarah', 'Ratcliffe'): [' Ph.D.', 'Associate Professor of Biostatistics', 'sratclif@upenn.edu']  
           ('Wei', 'Yang'): [' Ph.D.', 'Assistant Professor of Biostatistics', 'weiyang@mail.med.upenn.edu']  
      ('Matthew', 'Bryan'): [' PhD', 'Assistant Professor of Biostatistics', 'bryanma@upenn.edu']  
    ('Benjamin', 'French'): [' PhD', 'Associate Professor of Biostatistics', 'bcfrench@mail.med.upenn.edu']  
          ('Dawei', 'Xie'): [' PhD', 'Assistant Professor of Biostatistics', 'dxie@upenn.edu']  
   ('Kathleen', 'Propert'): [' Sc.D.', 'Professor of Biostatistics', 'propert@mail.med.upenn.edu']  
       ('Wensheng', 'Guo'): [' Ph.D', 'Professor of Biostatistics', 'wguo@mail.med.upenn.edu']  
    ('Phyllis', 'Gimotty'): [' Ph.D', 'Professor of Biostatistics', 'pgimotty@upenn.edu']  
        ('Pamela', 'Shaw'): [' PhD', 'Assistant Professor of Biostatistics', 'shawp@upenn.edu']  
    ('Jonas', 'Ellenberg'): [' Ph.D.', 'Professor of Biostatistics', 'jellenbe@mail.med.upenn.edu']  
   ('Scarlett', 'Bellamy'): [' Sc.D.', 'Associate Professor of Biostatistics', 'bellamys@mail.med.upenn.edu']  
      ('Michelle', 'Ross'): [' PhD', 'Assistant Professor is Biostatistics', 'michross@upenn.edu']  
         ('Jinbo', 'Chen'): [' Ph.D.', 'Associate Professor of Biostatistics', 'jinboche@upenn.edu']  
           ('Rui', 'Feng'): [' Ph.D', 'Assistant Professor of Biostatistics', 'ruifeng@upenn.edu']  
     ('Marshall', 'Joffe'): [' MD MPH Ph.D', 'Professor of Biostatistics', 'mjoffe@mail.med.upenn.edu']  
     ('Wei-Ting', 'Hwang'): [' Ph.D.', 'Associate Professor of Biostatistics', 'whwang@mail.med.upenn.edu']  
         ('Mingyao', 'Li'): [' Ph.D.', 'Associate Professor of Biostatistics', 'mingyao@mail.med.upenn.edu']  
          ('Jason', 'Roy'): [' Ph.D.', 'Associate Professor of Biostatistics', 'jaroy@mail.med.upenn.edu']  
     ('Alisa', 'Stephens'): [' Ph.D.', 'Assistant Professor of Biostatistics', 'alisaste@mail.med.upenn.edu']  
    ('Rebecca', 'Hubbard'): [' PhD', 'Associate Professor of Biostatistics', 'rhubb@mail.med.upenn.edu']  
   ('Knashawn', 'Morales'): [' Sc.D.', 'Associate Professor of Biostatistics', 'knashawn@mail.med.upenn.edu']  
         ('Sharon', 'Xie'): [' Ph.D.', 'Associate Professor of Biostatistics', 'sxie@mail.med.upenn.edu']  
      ('Andrea', 'Troxel'): [' ScD', 'Professor of Biostatistics', 'atroxel@mail.med.upenn.edu']  
        ('Yenchih', 'Hsu'): [' Ph.D.', 'Assistant Professor of Biostatistics', 'hsu9@mail.med.upenn.edu']  
          ('J.', 'Landis'): [' B.S.Ed. M.S. Ph.D.', 'Professor of Biostatistics', 'jrlandis@mail.med.upenn.edu']  
  ('Russell', 'Shinohara'): ['0', 'Assistant Professor of Biostatistics', 'rshi@mail.med.upenn.edu']  
        ('Mary', 'Sammel'): [' Sc.D.', 'Professor of Biostatistics', 'msammel@cceb.med.upenn.edu']  
      ('Warren', 'Bilker'): ['Ph.D.', 'Professor of Biostatistics', 'warren@upenn.edu']  
         ('A.', 'Localio'): [' JD MA MPH MS PhD', 'Associate Professor of Biostatistics', 'rlocalio@upenn.edu']  
      ('Haochang', 'Shou'): [' Ph.D.', 'Assistant Professor of Biostatistics', 'hshou@mail.med.upenn.edu']  
      ('Nandita', 'Mitra'): [' Ph.D.', 'Associate Professor of Biostatistics', 'nanditam@mail.med.upenn.edu']  
          ('Mary', 'Putt'): [' PhD ScD', 'Professor of Biostatistics', 'mputt@mail.med.upenn.edu']  
  
dictionary comprehension used to provide first name as key  
     Sarah: [' Ph.D.', 'Associate Professor of Biostatistics', 'sratclif@upenn.edu']  
    Sharon: [' Ph.D.', 'Associate Professor of Biostatistics', 'sxie@mail.med.upenn.edu']  
   Russell: ['0', 'Assistant Professor of Biostatistics', 'rshi@mail.med.upenn.edu']  
  Kathleen: [' Sc.D.', 'Professor of Biostatistics', 'propert@mail.med.upenn.edu']  
       Wei: [' Ph.D.', 'Assistant Professor of Biostatistics', 'weiyang@mail.med.upenn.edu']  
  Haochang: [' Ph.D.', 'Assistant Professor of Biostatistics', 'hshou@mail.med.upenn.edu']  
   Matthew: [' PhD', 'Assistant Professor of Biostatistics', 'bryanma@upenn.edu']  
   Hongzhe: [' Ph.D', 'Professor of Biostatistics', 'hongzhe@upenn.edu']  
    Pamela: [' PhD', 'Assistant Professor of Biostatistics', 'shawp@upenn.edu']  
      Mary: [' PhD ScD', 'Professor of Biostatistics', 'mputt@mail.med.upenn.edu']  
  Scarlett: [' Sc.D.', 'Associate Professor of Biostatistics', 'bellamys@mail.med.upenn.edu']  
  Benjamin: [' PhD', 'Associate Professor of Biostatistics', 'bcfrench@mail.med.upenn.edu']  
       Rui: [' Ph.D', 'Assistant Professor of Biostatistics', 'ruifeng@upenn.edu']  
        A.: [' JD MA MPH MS PhD', 'Associate Professor of Biostatistics', 'rlocalio@upenn.edu']  
   Mingyao: [' Ph.D.', 'Associate Professor of Biostatistics', 'mingyao@mail.med.upenn.edu']  
     Jonas: [' Ph.D.', 'Professor of Biostatistics', 'jellenbe@mail.med.upenn.edu']  
     Alisa: [' Ph.D.', 'Assistant Professor of Biostatistics', 'alisaste@mail.med.upenn.edu']  
   Phyllis: [' Ph.D', 'Professor of Biostatistics', 'pgimotty@upenn.edu']  
    Andrea: [' ScD', 'Professor of Biostatistics', 'atroxel@mail.med.upenn.edu']  
   Rebecca: [' PhD', 'Associate Professor of Biostatistics', 'rhubb@mail.med.upenn.edu']  
   Nandita: [' Ph.D.', 'Associate Professor of Biostatistics', 'nanditam@mail.med.upenn.edu']  
  Michelle: [' PhD', 'Assistant Professor is Biostatistics', 'michross@upenn.edu']  
  Wei-Ting: [' Ph.D.', 'Associate Professor of Biostatistics', 'whwang@mail.med.upenn.edu']  
     Susan: [' Ph.D.', 'Professor of Biostatistics', 'sellenbe@upenn.edu']  
     Jinbo: [' Ph.D.', 'Associate Professor of Biostatistics', 'jinboche@upenn.edu']  
   Yenchih: [' Ph.D.', 'Assistant Professor of Biostatistics', 'hsu9@mail.med.upenn.edu']  
     Yimei: [' Ph.D.', 'Assistant Professor of Biostatistics', 'liy3@email.chop.edu']  
     Jason: [' Ph.D.', 'Associate Professor of Biostatistics', 'jaroy@mail.med.upenn.edu']  
  Knashawn: [' Sc.D.', 'Associate Professor of Biostatistics', 'knashawn@mail.med.upenn.edu']  
  Marshall: [' MD MPH Ph.D', 'Professor of Biostatistics', 'mjoffe@mail.med.upenn.edu']  
   Justine: [' Ph.D.', 'Professor of Biostatistics', 'jshults@mail.med.upenn.edu']  
  Wensheng: [' Ph.D', 'Professor of Biostatistics', 'wguo@mail.med.upenn.edu']  
        J.: [' B.S.Ed. M.S. Ph.D.', 'Professor of Biostatistics', 'jrlandis@mail.med.upenn.edu']  
     Dawei: [' PhD', 'Assistant Professor of Biostatistics', 'dxie@upenn.edu']  
    Warren: ['Ph.D.', 'Professor of Biostatistics', 'warren@upenn.edu']  
```

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> There were 937 days between 01-02-2013 and 07-28-2015.

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> There were 513 days between 12-31-2013 and 05-28-2015.

c.  
```
date_start = '15-Jan-1994'
date_stop = '14-Jul-2015'
```

>> There were 7850 days between 15-Jan-1994 and 14-Jul-2015.


Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





