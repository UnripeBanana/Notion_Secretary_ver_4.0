def trade_updator(results):
    for id, raw_prop in results.items():
        properties = {
            "잔량": {"number": raw_prop["remaining"]},
            "실현수익": {"number": raw_prop["profit"]}
        }

        if raw_prop["profit"] and not raw_prop["profit_saved"]: 
            net_profit("domestic_stock", raw_prop["profit"])
            properties["순수익 반영"] = {
                "checkbox": True
            }

        notion.pages.update(
            page_id = id,
            properties = properties
        )
