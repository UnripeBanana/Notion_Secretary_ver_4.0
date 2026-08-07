from notion.config import NOTION_TRADE_DB_ID
from notion.get_all_pages import get_all_pages
from collections import defaultdict
from notion.trade.fifo import process_fifo

#-----------------------------------------
# 국내주식 거래내역 DB 업데이트
#-----------------------------------------
from notion.trade.reader import trade_reader
from notion.trade.updator import trade_updator

# 각 페이지별로 데이터 읽기
trade_groups = defaultdict(list)

for page in get_all_pages(NOTION_TRADE_DB_ID):
    print(page["properties"])
    trade = read_trade_DB(page)  
    trade_groups[trade["ticker"]].append(trade)   
    
# 읽은 데이터 fifo처리
for trades in trade_groups.values():
    trades.sort(key=lambda x: x["date"])

trade_results = process_fifo(trade_groups)

# 노션에 데이터 업데이트
update_trade_DB(trade_results)
