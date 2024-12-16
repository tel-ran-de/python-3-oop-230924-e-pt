import pandas as pd


def main():
    df = pd.DataFrame({'name': ['name1', 'name2', 'name3', 'name4'], 'group': ['group1', 'group1', 'group2', 'group2'],
                       'знач 2': [1, 2, 34, 5], 'val2': [4, 6, 2, 7]}, index=[1, 2, 3, 4])

    # df = pd.DataFrame([{'name': 'task1', 'desc': 'desk1'}, {'name': 'task2', 'desc': 'desk2'}])

    print(df)

    print('\n')

    print(df.loc[df['group'] == 'group1'])

    # print(df)
    # print('\n')
    #
    # print(df.sort_values(by='знач 2'))
    #
    # print('\n')
    #
    # print(list(df.columns))
    #
    # print(df.columns[2])
    #
    # print('\n')
    # print(df.iloc[1]['val2'])
    #
    # print('\n')
    # print(df.shape[0])

    df.to_csv('test.csv')

    df = pd.read_csv('test.csv')



if __name__ == "__main__":
    main()
