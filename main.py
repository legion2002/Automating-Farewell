import pygsheets
import pandas as pd
gc = pygsheets.authorize("client_secret.json")
sh = gc.open("Test spreadsheet")
order = sh[0]
messages = sh[1]
test = sh[2]
order_df = order.get_as_df()
messages_df = messages.get_as_df()
# print(order_df)
name = order_df["Name"][2]
match_df = messages_df[messages_df["Who is this message for? (Please add full name)"].str.contains(name)]
print(match_df)
final = ''
for ind in match_df.index:
    print(ind)
    sender = messages_df.at[ind,"Your Name"]
    text = messages_df.at[ind,"Your message:"]
    final += f"\n {sender}: {text} \n"
test.update_value("A1",final)
i = 2
for name in order_df["Name"]:
    if(name != ""):
        match_df = messages_df[messages_df["Who is this message for? (Please add full name)"].str.contains(name)]
        # print(match_df)
        final = ''
        for ind in match_df.index:
            print(ind)
            sender = messages_df.at[ind, "Your Name"]
            text = messages_df.at[ind, "Your message:"]
            messages.update_value(f"I{ind}", 1)

            final += f"\n{sender}: \"{text}\" \n"
        test.update_value(f"B{i}", final)
        test.update_value(f"A{i}",  name)
        order.update_value(f"I{i}", final)

    else:
        order.update_value(f"I{i}", "None")
        test.update_value(f"B{i}", "None")

    i += 1
#
# personlist = order_df["Name"]
# personMessages = (messages_df["Who is this message for? (Please add full name)"],messages_df["Your message:"])
# i = 1
# for person in personlist:
#     for msgperson in personMessages:
#         i += 1
#
#         if(person == msgperson):
#             test.update_value(f"A{i}","success")


