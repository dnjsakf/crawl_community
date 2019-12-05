def getContents( community=None, cate=None, limit=5 ):
    pipelines = []

    match = { "$match": {
        "completed": { "$exists": False }
        , "link": { "$ne": "https://www.ygosu.comjavascript:;" }
    } }
    if community: match["$match"].update({ "community": community })
    if cate: match["$match"].update({ "cate": cate })

    addFields = { 
        "$addFields": {
            "_id": { "$toString": "$_id" }
            , "no": { "$toInt": "$no" }
        }
    }
    project = {
        "$project": {
            "link": 1
            , "_id": 1
            , "adult": 1
            , "login_path": 1
        }
    }
    sort = { 
        "$sort": { 
            "no": -1 
        }
    }
    limit = {
        "$limit": limit
    }

    return [ match, addFields, project, sort, limit ]

