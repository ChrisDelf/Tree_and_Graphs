int electionsWinners(int[] votes, int k)
{
    int max = Arrays.stream(votes).max().getAsInt();
    return k == 0 ? Arrays.stream(votes).filter(x -> x == max).count() == 1 ? 1 : 0 : (int) Arrays.stream(votes).filter(x -> x + k > max).count();
}

