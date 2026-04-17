class matrix 
{
    public boolean findRotation(int[][] mat, int[][] target) 
    {
        for (int i=0; i<mat.length; i++)
        {
            for(int j=i; j<mat.length; j++)
            {
                if(mat[i][j] == target[i][j])
                {
                    return false;
                }
            }
        } 
        return true;   
    }

    matrix sol = new matrix();
        sol.findRotation.mat = new int[][] {
            {
                0,
                1
            }, {
                1,
                0
            }
        };
        sol.findRotation.target = new int[][] {
            {
                1,
                0
            }, {
                0,
                1
            }
        };
        sol.findRotation(sol.findRotation.mat, sol.findRotation.target);
}