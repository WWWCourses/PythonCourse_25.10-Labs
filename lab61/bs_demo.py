from bs4 import BeautifulSoup as bs
import re

html = """
	<table width="660" cellspacing="0" cellpadding="0" border="0" style="margin-bottom:0px; border-top:#990000 1px solid;">
    <tbody><tr><td colspan="4"><img src="../images/picturess/no.gif" width="1" height="10" border="0"></td></tr>
    <tr>
      <td rowspan="2" valign="top" width="220">

      <table width="212" cellspacing="0" cellpadding="0" border="0">
        <tbody><tr>
          <td align="center" valign="top"><a href="//www.imot.bg/pcgi/imot.cgi?act=5&amp;adv=1j165227587917128&amp;slink=84hsv1&amp;f1=8" class="photoLink"><img src="//imotstatic1.focus.bg/imot/photosimotbg/1/128/1j165227587917128_lb.jpg" style="object-fit: cover;" width="200" height="150" border="0" alt="Обява продава къща, с. Лещен, област Благоевград"></a></td>
        </tr>
      </tbody></table>


      </td>
      <td valign="top" width="270" height="40" style="padding-left:4px">
        <div class="price">69 000 EUR<a href="javascript:;" id="star_1j165227587917128" onclick="javascript:openLogPopup(1); return false;" title="Добави обявата в бележника. Изисква регистрация." class="favListItem"></a> </div><br>
        <a href="//www.imot.bg/pcgi/imot.cgi?act=5&amp;adv=1j165227587917128&amp;slink=84hsv1&amp;f1=8" class="lnk1">Продава КЪЩА</a><br>
        <a href="//www.imot.bg/pcgi/imot.cgi?act=5&amp;adv=1j165227587917128&amp;slink=84hsv1&amp;f1=8" class="lnk2">с. Лещен, област Благоевград</a>
      </td>
      <td align="right" valign="top" width="60" height="40">
        &nbsp;
      </td>
      <td align="right" valign="top" width="110" height="40">
        <a href="//pirin_realty.imot.bg" class="logoLink" target="_blank"><img src="../images/logos/med/pirin_realty.pic" style="width:100px; height: 37px; object-fit: contain;" border="0" alt="Детайлен преглед"></a>
      </td>
    </tr>
    <tr>
      <td width="520" colspan="3" height="50" style="padding-left:4px">
        180 кв.м, двор 250 кв.м, Автентична възрожденска къща с РЗП от 180 кв.м. с 250кв.м. парцелно място в старобитното село Лещен. ..., тел.: 0895670590
      </td>
    </tr>

    <tr><td colspan="4"><img src="../images/picturess/no.gif" width="1" height="5" border="0"></td></tr>
    <tr>
      <td colspan="4">
        <table width="660" cellspacing="0" cellpadding="0" border="0">
          <tbody><tr>
            <td width="330" style="padding-left:4px">
              <a href="//www.imot.bg/pcgi/imot.cgi?act=5&amp;adv=1j165227587917128&amp;slink=84hsv1&amp;f1=8" class="lnk3">Повече детайли и 15 снимки</a> | <a href="javascript:;" id="notepad_1j165227587917128" onclick="javascript:openLogPopup(1); return false;" title="Добави обявата в бележника. Изисква регистрация." class="lnk3">Добави в бележника</a>
            </td>
            <td width="330" align="right">
              <a href="javascript:;" class="lnk3" onclick="javascript:mark(p1j165227587917128)">Маркиране/Размаркиране на Обявата</a> <a href="javascript:;" class="lnk3"><img name="p1j165227587917128" src="../images/picturess/print_n.gif" width="15" height="14" border="0" alt="МАРКИРАЙ ОБЯВАТА" onclick="javascript:mark(p1j165227587917128)" align="absmiddle"></a>
            </td>
          </tr>
        </tbody></table>
      </td>
    </tr>
    <tr><td colspan="4"><img src="../images/picturess/no.gif" width="1" height="10" border="0"></td></tr>
  </tbody></table>
"""


soup = bs(html, 'html.parser')
# get element by content:
el = soup.find(string=re.compile(r'.*продава.*',re.I))
print(el.parent)