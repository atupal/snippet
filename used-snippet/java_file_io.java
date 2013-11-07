package org.atupal.app;

import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.BufferedInputStream;
import java.io.DataInputStream;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;

import static java.lang.System.out;

public class App 
{
  public static void craetefile() {
    try {
      File file = new File("/tmp/file_test");
      file.createNewFile();
    } catch (Exception e) {
      e.printStackTrace();
    }
  }

  public static void readFileByBufferInputSteam() {
    try {
      File file = new File("/tmp/file_test");
      FileInputStream fis = new FileInputStream(file);
      BufferedInputStream bis = new BufferedInputStream(fis);
      DataInputStream dis = new DataInputStream(bis);
      while (dis.available() != 0) {
        out.println(dis.readLine());
      }
    } catch (Exception e) {
      e.printStackTrace();
    }
  }

  public  static void readFileByBufferReader() {
    // in java 7 you can use try-with-resource feature to close file
    // automatically try ( statement ) ...
    
    try {
      BufferedReader br = new BufferedReader( new FileReader("/tmp/file_test") );
      String line;
      while ( (line = br.readLine()) != null ) {
        out.println(line);
      }
    } catch (Exception e) {
      e.printStackTrace();
    }
  }


  public static void writeFileByOutputsteam() {
    try {
      File file = new File("/tmp/file_test");
      FileOutputStream fop = new FileOutputStream(file);

      if (!file.exists()) {
        file.createNewFile();
      } 
      byte contentInBytes[] = "content".getBytes();
      fop.write(contentInBytes);
      fop.flush();
      fop.close();
    } catch (Exception e) {
      e.printStackTrace();
    }
  }

  public static void writeFileByBufferedWriter() {
    try {
      File file = new File("/tmp/file_test");
      if (!file.exists()) {
        file.createNewFile();
      }
      // if you want append file content you need FileWriter(
      // file.getNmae(), true );
      FileWriter fw = new FileWriter(file.getAbsoluteFile());
      BufferedWriter bw = new BufferedWriter(fw);
      bw.write("content");
      bw.close();
    } catch (Exception e) {
      e.printStackTrace();
    }
  }

  public static void consoleReader() {
    try {
      BufferedReader br = new BufferedReader( new InputStreamReader(System.in) );
      String input;
      while ( (input = br.readLine()) != null ) {
        out.println(input);
      }
    } catch (Exception e) {
      e.printStackTrace();
    }
  }

  public static void main( String[] args ) {
    readFileByBufferReader();
  }
}
