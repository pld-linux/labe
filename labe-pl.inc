<?php

    // foot.tpl
    $smarty->assign("FOOT_AUTHOR","Stworzone przez Savoir-faire Linux i Mathieu Leduc-Hamel");

    // options.tpl
    $smarty->assign("OPT_MAIN_TITLE","LABE - Okno Po³±czenia");
    $smarty->assign("OPT_ERROR_CONNECT","Nie mo¿na siê po³±czyæ z hostem LDAP, proszê sprawdziæ konfiguracje");
    $smarty->assign("OPT_ERROR_CONFIG","Niezdefiniowano ¿adnego hosta LDAP w konfigyracji LABE skontaktuj sie z administratorem");
    $smarty->assign("OPT_CHOICE_DESC","Wybie¿ swój host LDAP i podaj has³o do serwera:");
    $smarty->assign("OPT_CHOICE_SERVER","Wybór serwera:");
    $smarty->assign("OPT_CHOICE_PASS","Has³o:");
    $smarty->assign("OPT_CHOICE_LANG","Jêzyk");
    $smarty->assign("OPT_BUTTON_CANCE","Anuluj");
    $smarty->assign("OPT_BUTTON_OK","Ok");

    // list.tpl
    $smarty->assign("LIST_BUTTON_ADD","Dodaj");
    $smarty->assign("LIST_BUTTON_REFRESH","Od¶wie¿");
    $smarty->assign("LIST_BUTTON_EXPORT","Eksportuj");
    $smarty->assign("LIST_BUTTON_IMPORT","Importuj");
    $smarty->assign("LIST_BUTTON_OPTIONS","Opcje");
    $smarty->assign("LIST_BUTTON_SEARCH","Szukaj");
    $smarty->assign("LIST_BUTTON_EXIT","Wyjd¼");
    $smarty->assign("LIST_BUTTON_PRINT","Drukuj");
    $smarty->assign("LIST_BUTTON_DEL","Usuñ");
    $smarty->assign("LIST_SEARCH_OPT_SN","Nazwisko");
    $smarty->assign("LIST_SEARCH_OPT_GIVENNAME","Imiê");
    $smarty->assign("LIST_SEARCH_OPT_ORG","Firma");
    $smarty->assign("LIST_SEARCH_OPT_MAIL","Email");
    $smarty->assign("LIST_SEARCH_OPT_TEL","Telefon");
    $smarty->assign("LIST_SORT_OPT_SN","Nazwa");
    $smarty->assign("LIST_SORT_OPT_SN_TITLE","Sortuj wed³ug nazwy");
    $smarty->assign("LIST_SORT_OPT_ORG","Firma");
    $smarty->assign("LIST_SORT_OPT_ORG_TITLE","Sortuj wed³ug firm");
    $smarty->assign("LIST_SORT_OPT_MAIL","Email");
    $smarty->assign("LIST_SORT_OPT_MAIL_TITLE","Sortuj wed³ug email'a");
    $smarty->assign("LIST_SORT_OPT_TEL","Telefon");
    $smarty->assign("LIST_SORT_OPT_TEL_TITLE","Wosrtuj wed³ug telefonu");
    $smarty->assign("LIST_MSG_NO_CONTACT","Nie ma ¿adnego kontaktu w bazie LDAP");

    // form (detail.tpl and new.tpl)
    $smarty->assign("FORM_BUTTON_RETURN","Cofnij");
    $smarty->assign("FORM_BUTTON_MODIFY","Modyfikuj");
    $smarty->assign("FORM_BUTTON_DEL","Usuñ");
    $smarty->assign("FORM_BUTTON_ADD","Dodaj");
    $smarty->assign("FORM_SECT_PRIVATE","Prywatne");
    $smarty->assign("FORM_ENTRY_PR__FIRST_NAME","Imiê");
    $smarty->assign("FORM_ENTRY_PR_LAST_NAME","Nazwisko");
    $smarty->assign("FORM_ENTRY_PR_INITIALS","Inicja³y");
    $smarty->assign("FORM_ENTRY_PR_MAIL","Email");
    $smarty->assign("FORM_ENTRY_PR_PIC","Zdjêcie");
    $smarty->assign("FORM_ENTRY_PR_ERASE_","Usuñ zdjêcie");
    $smarty->assign("FORM_SECT_HOUSE","Dom");
    $smarty->assign("FORM_ENTRY_HO_ADDRESS","Adres");
    $smarty->assign("FORM_ENTRY_HO_TEL","Telefon");
    $smarty->assign("FORM_ENTRY_HO_FAX","Fax");
    $smarty->assign("FORM_ENTRY_HO_CEL","Komórka");
    $smarty->assign("FORM_SECT_JOB","Praca");
    $smarty->assign("FORM_ENTRY_JB_CIE","Firma");
    $smarty->assign("FORM_ENTRY_JB_ADR","Adres");
    $smarty->assign("FORM_ENTRY_JB_CITY","Miasto");
    $smarty->assign("FORM_ENTRY_JB_STATE","Woj.");
    $smarty->assign("FORM_ENTRY_JB_CODE_POSTAL","Kod Pocztowy");
    $smarty->assign("FORM_ENTRY_JB_COUNTRY","Kraj");
    $smarty->assign("FORM_ENTRY_JB_WEB","Strona Domowa");
    $smarty->assign("FORM_ENTRY_JB_TITLE","Tytu³");
    $smarty->assign("FORM_ENTRY_JB_DEP","Oddzia³");
    $smarty->assign("FORM_ENTRY_JB_OFFICE","Biuro");
    $smarty->assign("FORM_ENTRY_JB_BOS","Szef");
    $smarty->assign("FORM_ENTRY_JB_TEL","Telefon");
    $smarty->assign("FORM_ENTRY_JB_FAX","Fax");
    $smarty->assign("FORM_ENTRY_JB_PAGE","Pager");
    $smarty->assign("FORM_ENTRY_JB_IP_PHONE","Telefon IP");
    $smarty->assign("FORM_SECT_OTHERS","Inne");
    $smarty->assign("FORM_ENTRY_OT_NETMEET","NetMeeting");
    $smarty->assign("FORM_ENTRY_OT_COMMENTS","Komentarz");
    $smarty->assign("FORM_MSG_NO_INFO","B³±d, nie ma ¿adnych informacji na temat tej osoby w bazie LDAP");

    // print.tpl
    $smarty->assign("PRINT_BUTTON_RETURN","Wstecz");
    $smarty->assign("PRINT_BUTTON_PRINT","Drukuj");
    $smarty->assign("PRINT_COL_NAME","Nazwisko, imie");
    $smarty->assign("PRINT_COL_CIE","Firma");
    $smarty->assign("PRINT_COL_EMAIL","Email");
    $smarty->assign("PRINT_COL_TEL","Telefon");
    $smarty->assign("PRINT_MSG_NO_CONTACT","Brak kontaktów w bazie LDAP");

    // import.tpl
    $smarty->assign("IMPT_MSG_BAD_FILE","Plik LDIF jest niepoprawny");
    $smarty->assign("IMPT_TITLE","LABE - Okno importowania kontaktów");
    $smarty->assign("IMPT_SUB_TITLE_FILE","Wybierz poprawny plik LDIF");
    $smarty->assign("IMPT_BUTTON_IMPT","Importuj");
    $smarty->assign("IMPT_TITLE_RESULT","Wynik importowania pliku");
    $smarty->assign("IMPT_WARN_CONTACT",
	"- Zosta³y zaimoprtowane tylko kontakty z podanym imieniem i nazwiskiem -");
    $smarty->assign("IMPT_COL_NAME","Imiê");
    $smarty->assign("IMPT_COL_KEEP_IT","Zachowaæ ?");
    $smarty->assign("IMPT_MSG_NO_CONTACT","Nie zaimportowano ¿adnego kontaktu");
    $smarty->assign("IMPT_BUTTON_CANCEL","Anuluj");
    $smarty->assign("IMPT_BUTTON_Ok","Ok");
?>
