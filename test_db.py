from pymongo import MongoClient
from pymongo.errors import OperationFailure

def check_mongo_connection(client_uri):
    connection = MongoClient(client_uri)

    try:
        print(connection.database_names())
        print('Data Base Connection Established........')

    except OperationFailure as err:
        print(f"Data Base Connection failed. Error: {err}")

#client_uri = "mongodb+srv://atlasadmin:yhPXQYuFvinQQFiS@cluster0.uydsz.mongodb.net/demodb?retryWrites=true&w=majority"
client_uri = "mongodb://mlwlite-backenddb-prod:hEzW01OlR00yfQ75ZgkMu31EePmXrFBXvzZqFBl2xPQqb2R3R5bft0XOgI4Bn8PSHyEUy2fxPKEB1DShq59Ltw==@mlwlite-backenddb-prod.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@mlwlite-backenddb-prod@"
#client_uri="mongodb://mlw-lite:z2XkUqu5HLhn4e0x8ULMkKfPJbHoPi6kll0tDxHrkGIsWqTcPrbMEslDpm2nRC2QnDxEPHRAKZn4nQp1nvC28w==@mlw-lite.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@mlw-lite@"
#client_uri="mongodb://mlwlite-backenddb-qa:veZVpj0uGmLdDZjcWf7VCOgSEJxVMEY6iK087afKvcMpcjDV96v2p037xV4LtNhTSZF3IXMt0quZbtnOYQHWRw==@mlwlite-backenddb-qa.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@mlwlite-backenddb-qa@"
client_uri="mongodb://mlw-backenddb-qa:yXya6ttfWZmLchv6hQQBrNpyJr1E4zaypH4jXHdIRTd1cbvDD80lrUb2W7rIbcg4GaLTwrqKn84TdkeJ2FsxZQ==@mlw-backenddb-qa.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@mlw-backenddb-qa@"
check_mongo_connection(client_uri)
