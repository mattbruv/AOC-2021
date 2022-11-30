.data
.align 4
nums:
.long 1974
.long 1902
.long 1356
.long 1724
.long 1550
.long 1870
.long 1436
.long 1945
.long 1640
.long 1766
.long 1508
.long 1802
.long 1495
.long 1837
.long 131
.long 1754
.long 1296
.long 1627
.long 1768
.long 1451
.long 1252
.long 1566
.long 1611
.long 1531
.long 1868
.long 1745
.long 1894
.long 1799
.long 1948
.long 1930
.long 1400
.long 2003
.long 1777
.long 1279
.long 472
.long 1474
.long 1787
.long 1406
.long 1522
.long 1646
.long 1865
.long 1581
.long 1609
.long 1705
.long 1383
.long 1276
.long 1613
.long 1190
.long 1856
.long 1528
.long 1091
.long 1540
.long 1720
.long 1824
.long 1734
.long 1919
.long 1681
.long 1686
.long 1344
.long 1644
.long 1670
.long 1710
.long 1708
.long 1458
.long 1728
.long 1972
.long 1630
.long 1995
.long 1763
.long 1935
.long 451
.long 1392
.long 1990
.long 14
.long 1893
.long 1437
.long 1632
.long 1933
.long 1887
.long 1975
.long 1453
.long 1897
.long 2005
.long 2008
.long 1959
.long 1716
.long 1635
.long 1619
.long 1994
.long 1674
.long 1942
.long 1817
.long 1825
.long 196
.long 769
.long 1065
.long 1662
.long 1079
.long 1574
.long 1554
.long 1621
.long 1857
.long 1312
.long 1544
.long 2001
.long 1991
.long 1602
.long 1669
.long 1982
.long 1309
.long 1556
.long 1855
.long 1284
.long 1641
.long 1786
.long 735
.long 1921
.long 1661
.long 1934
.long 1552
.long 1012
.long 1748
.long 1782
.long 1631
.long 1607
.long 1659
.long 1997
.long 1600
.long 1594
.long 1798
.long 1405
.long 1790
.long 1993
.long 1960
.long 1717
.long 999
.long 1687
.long 1771
.long 1977
.long 1809
.long 1884
.long 1795
.long 1639
.long 1565
.long 1299
.long 1643
.long 1700
.long 2002
.long 1823
.long 1369
.long 1572
.long 1657
.long 1683
.long 1966
.long 1606
.long 1792
.long 1756
.long 1936
.long 1718
.long 2009
.long 1711
.long 1461
.long 1638
.long 1645
.long 1914
.long 1963
.long 1546
.long 1846
.long 1737
.long 1788
.long 1589
.long 1860
.long 1830
.long 1905
.long 1571
.long 1989
.long 1780
.long 1878
.long 1767
.long 1776
.long 1727
.long 1582
.long 1769
.long 1040
.long 694
.long 1327
.long 1623
.long 1688
.long 1694
.long 1932
.long 2000
.long 1969
.long 1590
.long 1425
.long 1917
.long 1324
.long 1852
.long 1753
.long 1743
.long 1551

i: .long 0

j: .long 0

# 200 entries


# RSP = nums

.text
.global main
main:

    # load n1,
    # load n2,
    # see if they sum to 2020
    # if yes, multiply them and return
    # if no, increment n2

    # inc N2:
    # if n2 == 199
    # set n2 = 0, inc n1, restart

    movq $4, %rax
    push %rax # 8(rsp) = i
    push %rax #  (rsp) = j

    leaq nums(%rip), %rax
    # add sp offset
    addq (%rsp), %rax
    movl (%rax), %eax

    # Pop 2 quads off of stack to reset it
    addq $16, %rsp
    ret


#   load base address of nums into rax
#   leaq nums(%rip), %rax



