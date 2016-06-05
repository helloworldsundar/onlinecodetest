

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class TwoDArrayDS {

       public static void main(String[] args) 
       {
           Scanner in = new Scanner(System.in);
           int arr[][] = new int[6][6];
           for(int arr_i=0; arr_i < 6; arr_i++){
               for(int arr_j=0; arr_j < 6; arr_j++){
                   arr[arr_i][arr_j] = in.nextInt();
               }
           }

           int result = getHourGlassSum(arr,0,0,3);
           System.out.println("Sum of hourglass"+result);
       }
       
       /**
        * 
        * @param arr  - input array with hour glass
        * @param positioni - position from which hour glass has to be built
        * @param positionj - position j
        * @param hrSize  - hour glass size width - size 3 here
        * @return
        */
       public static int getHourGlassSum (int[][] arr,int positioni,int positionj,int hrSize)
       {
          int sumOfHourGlass = 0;
          int median = getMedian(hrSize);
          
          for (int iteration = 1; iteration <= hrSize; iteration++)
          {
             if (iteration == median)
             {
                sumOfHourGlass += arr[positioni+1][positionj];
             }
             sumOfHourGlass += arr[positioni][positionj];
             sumOfHourGlass += arr[positioni+2][positionj];

             positionj++; // traverse the column in matrix for getting other elems from hr glass
          }
             
          
          try
          {
             
          }catch(ArrayIndexOutOfBoundsException exec)
          {
             // So Hour Glass cannot be prepared at this index
             //mark sum as '0' as this point and return
             sumOfHourGlass = 0;
             // Note : explicitly set sumOfHourGlass as 0 , because
             // it may include partial Sum  from the point of Assumption
             // an hour glass exists
          }
          
          return sumOfHourGlass;
       }
       
       public static int getMedian (int value)
       {
          //if value is odd
          if (value%2 ==1)
          {
             return ((value+1)/2);
          }
          else
          {
             //if value is even
             return (value/2);
          }
       }
   }

