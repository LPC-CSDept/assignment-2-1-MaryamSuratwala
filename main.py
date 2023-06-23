def main():
    num_males = int(input('Enter number of Males: '))
    num_females = int(input('Enter number of Females: '))

    total = num_males + num_females
    m_perc = (num_males / total) * 100 
    f_perc = (num_females / total) * 100

    print(f'Total Number of Students {total}')
    print(f"Number of Males: {num_males} Number of Females: {num_females}")
    print("Percentage of males: {:.2f}%".format(m_perc), "Percentage of females: {:.2f}%".format(f_perc))
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
