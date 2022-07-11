import pandas

#dropping unnecessary columns
def drop_column(df):
    df.drop(["__version__","_status","_submission_time", "_submitted_by", "_uuid", "_xform_id_string", "formhub/uuid","meta/instanceID","point"], axis = 1, inplace=True)
    df.drop(list(df.filter(regex = "_attachments")), axis = 1, inplace = True)
    return(df)

#replacing _ with :
def replace_column(df):
    df.columns = df.columns.str.replace("_",":")
    return(df)

#changing capitalization 
def check_capital(df):
    i = 0 
    for column_name in df[['addr:street','addr:town','name']]:
        i=0
        column_all = df[column_name]
        for column_value in column_all:
            #
            print(str(column_value) + " Before")
            column_all[i] = str(column_value).title()
            print(str(column_all[i]) + " After")
            i = i+1
        df[column_name] = column_all
    return(df)

#OPENING CSV
df = pandas.read_csv("test.csv")

drop_column(df)
replace_column(df)
check_capital(df)

print(df)
#SAVING TO CSV
df.to_csv("new.csv",index=False)
