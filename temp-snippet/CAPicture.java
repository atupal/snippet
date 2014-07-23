/*
   get CA matric.
 */
import Jama.*; 
import Jama.Matrix;
import java.lang.*;

public class CAPicture {
    /*
        X1: ca matrix
        Y1: ca matrix
        explainRatio: 
     */
    private double explainRatio = 1.;
    private Matrix X;
    private Matrix X1;
    private Matrix Y1; 
    private double sum; 

    /*
       @param args: the arrays to build matrix
     */

    public CAPicture(double args[][]) {
        X = new Matrix(args);
        sum = 0;
        for (int i = 0; i < args.length; ++ i) {
            for (int j = 0; j < args[i].length; ++ j) {
                sum += args[i][j];
            }
        }
        init();
    }

    public CAPicture(double args[], int row, int col) {
        X = new Matrix(args, col);
        sum = 0;
        for (int i = 0; i < args.length; ++ i) {
            sum += args[i];
        }
        init();
    }

    private void init() {
        Matrix X1Y1[] = new Matrix[2];
        int nrow = X.getRowDimension();
        int ncol = X.getColumnDimension();

        Matrix P = X.times(1./sum);
        Matrix one = new Matrix(ncol, 1, 1);
        Matrix r = P.times(one);
        one = new Matrix(nrow, 1, 1);
        Matrix c = P.transpose().times(one);
        Matrix Z = diag(r, -.5).times(P.minus(r.times(c.transpose())))
            .times(diag(c, -.5));
        SingularValueDecomposition Z_svd = Z.svd();
        Matrix U = Z_svd.getU().getMatrix(0, nrow-1, 0, 1);
        Matrix V = Z_svd.getV().getMatrix(0, ncol-1, 0, 1);
        // ! call getS() will Throw ArrayIndexOutOfBoundsException.
        // Matrix SV = Z_svd.getS().getMatrix(0, 1, 0, 1);
        double sv[] = Z_svd.getSingularValues();
        
        double tmp = 0;
        for (int i = 0; i < sv.length; ++ i) {
            tmp += sv[i]*sv[i];
        }
        tmp = (sv[0]*sv[0] + sv[1]*sv[1]) / tmp;
        this.explainRatio = tmp;

        Matrix SV = diag(sv).getMatrix(0, 1, 0, 1);
        Matrix A = diag(r, .5).times(U);
        Matrix B = diag(c, .5).times(V);
        Matrix X1 = diag(r, -1).times(A).times(SV);
        Matrix Y1 = diag(c, -1).times(B).times(SV);
        X1Y1[0] = X1;
        X1Y1[1] = Y1;

        this.X1 = X1;
        this.Y1 = Y1;
    }

    public double getExplainRatio() {
        return this.explainRatio;
    }

    public Matrix getX1() {
        return this.X1;
    }

    public Matrix getY1() {
        return this.Y1;
    }

    private Matrix diag(Matrix r, double exp) {
        int row = r.getRowDimension();
        int col = r.getColumnDimension();
        int n = row + col - 1;
        Matrix dr = new Matrix(n, n);
        for (int i = 0; i < row; ++ i) {
            for (int j = 0; j < col; ++ j) {
                dr.set(i+j, i+j, Math.pow(r.get(i, j), exp));
            }
        }
        return dr;
    }

    private Matrix diag(Matrix r) {
        return this.diag(r, 1.);
    }

    private Matrix diag(double r[], double exp) {
        int n = r.length;
        Matrix dr = new Matrix(n, n);
        for (int i = 0; i < n; ++ i) {
            dr.set(i, i, Math.pow(r[i], exp));
        }
        return dr;
    }

    private Matrix diag(double r[]) {
        return this.diag(r, 1.);
    }

    public void printMatrix(Matrix m) {
        int row = m.getRowDimension();
        int col = m.getColumnDimension();
        for (int i =0; i < row; ++ i) {
            for (int j = 0; j < col; ++ j) {
                System.out.print(m.get(i, j));
                System.out.print("\t");
            }
            System.out.println();
        }
        System.out.println();
    }

    public static void main(String args[]) {
        double testMatrixArray[][] = {
            {2685,9252,9769,11465,8618,8291,4978},
            {926,10061,19884,19747,10050,5930,1485},
            {49,809,4620,14195,11847,11075,4769},
            {4,0,5,27,41,56,150}
        };
        CAPicture ca = new CAPicture(testMatrixArray);
        ca.printMatrix(ca.getX1());
        ca.printMatrix(ca.getY1());
        System.out.println(ca.getExplainRatio());
    }
}
