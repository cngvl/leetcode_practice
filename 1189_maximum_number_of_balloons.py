def maxNumberOfBalloons(text):
    # Iterate over the text string
    # Add some counter for each key letter: b a l o n
        # if b = 1
        # a = 1
        # l = 2
        # o = 2
        # n = 1
    # add 1 to return value
    # maybe make an array with the stored letters so it can pop out the letters after counted? - not sure how i'd pop out these values
    # alternative is to make a dictionary but not sure how to remove the key + values after
    # can add an until loop to count for letters after its been stored in a dictionary / array ?
    # return int

    noBalloons = 0
    balloonDict = {}
    for letter in text:
        if letter == "b" or letter == "a" or letter == "l" or letter == "o" or letter == "n":
        # if letter == "a" or letter == "l" or letter == "o" or letter == "n":
            # print(letter)
            if letter in balloonDict:
                balloonDict[letter] += 1
            else:
                balloonDict[letter] = 1

    # this feels kinda shitty
    # how to avoid error if balloondict[b] doesnt exist
    if 'b' and 'a' and 'l' and 'o' and 'n' in balloonDict:
        # for b in balloonDict:
        while balloonDict['b'] >= 1 and balloonDict['a'] >= 1 and balloonDict['l'] >= 2 and balloonDict['o'] >= 2 and balloonDict['n'] >= 1:
            if balloonDict['b'] >= 1 and balloonDict['a'] >= 1 and balloonDict['l'] >= 2 and balloonDict['o'] >= 2 and balloonDict['n'] >= 1:
                noBalloons += 1
                balloonDict['b'] -= 1
                balloonDict['a'] -= 1
                balloonDict['l'] -= 2
                balloonDict['o'] -= 2
                balloonDict['n'] -= 1
    print(balloonDict)
    return noBalloons


# text = "nlaebolko"
# >>> 1

# text = "loonbalxballpoon"
# >>> 2

# text = "leetcode"
# >>> 0

# text = "balloonballoonballoonballoonballoonballoon"
# >>> 6

# text = "balon"
# >>> 0
# infinite loopin

# text = "ghrylkxrmb"
# >>> 0

text = "rrnlnfevwkvhqzathacmhyhonsvcwmmmehcgchzfjvfoxbnagtxwnwcjcbmbgexqhlefjyrijwjolebtodxtapgyrzmgqzexvugtermrktyjbaicmskxmdopmtoxayydqjjogxmmmpvfiajknjfsikgrwsejzgnbsblsjkkcbaunqthiaetvxlylylzjqkvgysxfoltcmxwrtwpkvhofoaxdugfnsuhepfxudwllyiyrszrpwkwlvpsspvgcimcrngfllsjjdppihhczogfwegibuzzacojtruvozbqwikgdjeqxyarjwaawzictwpdruufifgbqzatmkkdnjajnklnzfdxcsjpmebjqpuqqamoexnnqxccngljzhnhbroyoaphgmksefhizibzpgehvtujmjdhskvpqicxbziqifjqqkaowileochjqhrccajnthqeqgwazedgehdtkwchxjjzcyjimrkykcvkfbzqiusgkxdilnfislphmeliqspvhuichuusqxnutiyxvdtgfnnrrkjwjmkjqjradnocssmfefgfgtzpbnlzxardrrrttnnqttnsowwrqswyqxhsxtlnfxogulwqhkowniohtznlyfjqlzvowcvqxynjpiyiggnxgtmyhjcbehxxsgltojszqyfpnsiybksmozwsqfxpvgeyoyeccxqlcziikavapxyjcftxhfimabmquzkyxnnablhpikwbwwmpjdtmukmuvcfkraqcbopufsaigskwgpjdubbympilgaojuvzgapairttwzuexbsigzcgerblgdgfwkiiqvokbmbtdzkakkeahkgjuyepvtbwqgerztvgunzhgitwottmejilmwyzwczjoxckyjtcbfsryofffaugsketifypahgqgmeypsyjvftqynbzhrobiwouuykyczskcdedidptykluykypnsfuudqgpqzwextbbumiuymngczkfrowkzxxtggqlwlaohfkgfmbyyaboapwhhopewnchlmvifpdkeovpjyugautultdbbxkjxqbcamrpqhndfeybwoatrjwvroakmqapknzzumapytdsdhhlstojlnlvpqjxlpbwfkdupgxzajyjrutzeljnmyxkcdrcjsxfmbqhzblnlqgsqzqjtiaelfkuoyjcjdlpvajkkgyuabgiwlybwmaqdtireukwieifvpzptnebjtwcvmhltkotrvkxcbbsehkdkiegzzbtszfdslqnecluxilqqgqwotfqqoogzzsyfdaujymrjfeoiqpzdeispqsnvlocqdyjcthtxlerjgowzfwsqgourkdhyfaaexjwnfppvrwhdbtsxqqqlrzvkergkxiqzlwdfomyreafirkaycmvjmwnnaqexoewwymvgsrajurzfiohzsbrehhnfghanczevwavsjjslwmnljlmixepwiwalqatgwfzzqhqvrrrhxleuzffgjuihnlbeukyapalwlfjtpumiexkwnvdxiikfajsbxcaywwjjqmgtzrihaoebjduvsmyfvjcthmbjjcausloupnqwjcncosrinvnspqwzlsrivpbpmgsoevunzthofjxspcgordbpudedcfdbbqvymtwujzdtcvigwuofoowqusrsavwkoyabsvllwpqidbpelffmrzfwdhaypxzwofssgkcqobnuomcejbuolmashglsiixcogolmgcmtauauhupkcqdhwesdmpnelcpvnyipakzlsbrpjppayzsremllqnmizvqcphkyuvwrqphdmgiwousanjuazlocddvgduoqmvfovidicmjufaytymcvoonvndbuuljgdvalsnypemzbwovgclcdfwcjptsbelifrqocsuwiwsyzrcxwuweiehtiegogvawkjogwtftbwabpcufuepabxxiqngntudhhuxrvhmhunepamdtfavtuajmrfvgirquwginxtjcmxgmstmhkqncpkdicemhcofqcbceiukstmjzsavwuhgpwbsymupyldwtsbvdjdevvgtddvqqcibnbseqgiaputwgapmovminivrbzlerjwsiofgiihyooqyjchcctvjfebhpvwncqhbleluycybaqlxikorlkqxwzmtrbgpwiqqormjftiarumgxeasqeusnewjqedzhiibbfurgbuwmxfycaevtijtttcbzvgumgiimwzjzpwhuqqwotjrlayrqwcwltiivumafhucrnzjqddvvtrxjsupfxlrohxmytridseyiajntpjsdrbdhdrtnackpytfuzkeiwgukwhvtvehvrdldfugtlwksywnuygichqnjbsmsupsowajduoukduoulagskxvxskewsyhsgakjyqeconciayfwqwdwdnilmllyuwqmatjzxyuhvujrcwkdybdmszzoxwzxojimlfqldxaiqgvziifuobnhonlafoulxgcorcclsxkrwrxinsadpgfmunwjdwgsiepbclggbqpxfjdxqseqidtgrqkixxwmblwokkupjqavvniwjyfuobcbhqfymrayevkteoaturjyvpbjaawgesxnwdvshiiijylclbqwjavftdmrrdsyhqcjweptywnqpcnzucqnzyyptaosrhvfzdomojkoeyepbpbfupkrnyzftjwpdgfqmwhjnhatsedirwzcpeppusaekjsbevlrzyxqtfgcnpszwxhgaeincudnfmcqawcnfkawjrguhitkqtxcxcvojgudfsrezcpfcntnezvskggzhisksxsehgzqxrrqtdlhjhgrblgnbfulmfawtfwnsrjixrjbwwxkvppjdtydgrsnmcpwcudxoiunilylpivbicvxwijrcxhflkznmskrbnighehsyrrzxazwyyvxgffmheubmogkdqtbeyoffgpuathllbiublcvkhzhogbspoogzobbbkylptbwxrbnbhevugkufrbrsgijcvylqeoucsomarwklmmztirevahocqoewrxojvfrakuevheeioirhgttufsxwfymwgxebtazonolntbhfwwgpmoluhnnzcwfhjoxthbuihecsxlfnexaghbaiawxfcsrznockvfoaemmizfltiebkoygchtspwcmijtjvrzljaovsbprmcsgwkqpvjtucemnpxxzzhpxvydfxsoyypecppdwwusbrgysxdaccafafoslqfcohtlgqcuojqwilxbsxrogyfcsqbxdqvdvpnjdeqmrcriczwviehftrhuwrguzrhukemyzeeworelrjwosskahsiazkpwvgscbihgnqtcoicapcsbvngvqgkqgvfuyhcoabpgrdqthxbalglvvrxifdzocgnweutsgrhmiuhoitrmccscophlcmarepzlisqdzidhocliidjikgzsmbjasukprfvlpkgryoyjtmuknjcmphkzhipocykitztqihhsjmxbrwefwgbdkdillzkosondaevcfyeikdfhgnughasibklabfwxkpxjpfwbjlczyusecvbyzlnxbhodtqpacvdgzzffxegivtemuswsmgiieldivzbildwucddnizmyofqtymmikpkzwohivqnipnwrdjatiyvlnrtwkrcrifmxvofolrbbhvyigrlsldqgbivahebsttymezbixrheczduzsqidjxfqorcxqssmcpnphnprpwlkyofnamfmezxoivrtxoxqralelxegltcpsleogdotrdgwxaspyghklhklbxsvfwjkbdjikdtzyhoufeqnqcmetpvvilyakjxmsoescrvivbslvdpunwhuylsgswgvfxfptnrskmsyiezttvwjwilhqdnpvayggvwepizpmjwhsellrypgtujbmqmpnngkwkgwrasmnomqhukusjadlpgpbhpnefhjippzhcdasuhauthuqbvvmndggmlckpjuuopsyrwtwkdtkwplrgfrgunfogevjqxqsoryjwmahmqhlgbyfqfgcfanjkerbirdilapihcrquviryewnphzwhsprelcnlgsczxonivmzknffspyeodsyxtkjcnljwfldvqwqndjcpxzxhjnsjuoedkrbmcsyyfhhjbvekmnfpxwchganhcmxbtoaofbbfvfewpzqrpgindhcqutdkyrtufdnsxxhachxvvfokczlrcdvygxusslaxllcspnbrtblgjlzmkxfpgeuepetuzesccdskwfunxaehfxsqopqjplukuivautozxtlujwxoijihzueabboyxvbtaangqzokdzwhbxodlfmryhikccbdprouslrgktmdjimvwshpbzvdmbtyyggnsamppcasbmdxlbsoosftfmamcmpvaojyfbwajwkodaokljngsknpklkticblmghnihdmezdyvriohgvvonutlmcfavvqndjnsskhamflpipuvusyqyzwlfrlestfppascaszytzagpcrwgeswhzuquurnytvrzsoyuqvjpwbmyksxueizewjmxnncniuddtmkpqhrzonwahjgmjxwihyalelbnwplqqhdgyrhcrnpdslxbdjhlmbvbvkwhjivspoejwtviwujcnuqjkskfpdnefruoyziynqcivjvlvaojhpcncbspuatgsyizklwfdbhwzbrbmxcyfxiwuwsorckrtdazaorauxmecsoywytrhuwqrobxndyfvwqukccpidvmecwuhdnqfsahqoxtswfdzzaystjmikdumrznihaakatobdrmjmahgefjomhywqfuiquafulpybnrvcfptttjaohipdrgbtvdzgxsakfvvoumdlalajlpusskjwlweufcjzpzhdcssqlkkrhaonmzxqtulrpqhubbgbagwyzpizbjegvjtqbkaiqididqvnbsknxegvkcfxdlljqs"
# >>> 98

print(maxNumberOfBalloons(text))
