import WhoAmI_File
def test_WhoAmI():
    assert WhoAmI_File.WhoAmI != 'djr2132'

test_WhoAmI()
        
import BondPrice_File
def test_getBondPrice():
    assert round(BondPrice_File.getBondPrice(.03, 2000000, .04, 10,  1)) == 2170604
    assert round(BondPrice_File.getBondPrice(.03, 2000000, .04, 10,  2)) == 2171686


test_getBondPrice()

import BondDuration_File
def test_getBondDuration():
    assert round(BondDuration_File.getBondDuration(.03, 2000000, .04, 10,1),2) == 8.51
test_getBondDuration()

import BondPrice_E_File
def test_GetBondPriceE():
    yc = [.010,.015,.020,.025,.030]
    face = 2000000
    couponRate = .04
    m = 10
    assert round(BondPrice_E_File.getBondPrice_E(face, couponRate, m, yc)) == 2098949

test_GetBondPriceE()

import BondPrice_Z_File
def test_GetBondPriceZ():
    yc = [.010,.015,.020,.025,.030]
    times=[1,1.5,3,4,7]
    face = 2000000
    couponRate = .04
    x = BondPrice_Z_File.getBondPrice_Z(face, couponRate, times, yc)
    assert round(x) == 1996533

test_GetBondPriceZ()

import FizzBuzz_File
def test_FizzBuzz():
    x = FizzBuzz_File.FizzBuzz(40,45)
    assert x[0] == "buzz"
    assert x[1] == 41
    assert x[5] == "fizzbuzz"

test_FizzBuzz()
