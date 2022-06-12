import pytest
import main

def test_col(capsys):
    main.col(0, 1)
    captured = capsys.readouterr()
    assert captured.out == "1, \n1, 1, \n"

def test_row(capsys):
    main.row(0,1,1)
    captured = capsys.readouterr()
    assert captured.out == "1, 1, "
