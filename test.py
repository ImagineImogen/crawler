import pytest
from search import Search
from scrapper import Scrapper

def test_search():
    sea = Scrapper().search("http://www.google.com")
    assert sea.find('<title>Google</title>') >= 0

def test_save_results():
    scrap = Scrapper()
    assert scrap.save_results("test") == 1

def test_display():
    disp = Scrapper()
    assert disp.display(10, "google") is None


def test_main():
    search = Search("test", 1, "google")
    assert search.main().find("<!doctype html><html lang=") >= 0
