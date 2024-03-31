package com.example.clientserver;

import android.os.Parcel;
import android.os.Parcelable;
import android.widget.EditText;
import android.widget.TextView;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.net.UnknownHostException;

public class Client implements Parcelable {
    String _userName;
    Socket socket;
    DataOutputStream out;
    DataInputStream in;

    public Client(String userName) {
        _userName = userName;
    }

    protected Client(Parcel in) {
        _userName = in.readString();
    }

    public static final Creator<Client> CREATOR = new Creator<Client>() {
        @Override
        public Client createFromParcel(Parcel in) {
            return new Client(in);
        }

        @Override
        public Client[] newArray(int size) {
            return new Client[size];
        }
    };

    public void listenSocket(){
        try{
            socket = new Socket("10.0.2.2", 12345);
            out = new DataOutputStream(socket.getOutputStream());
            in = new DataInputStream(socket.getInputStream());
            System.out.println("CONNECTION ESTABLISHED");
            out.writeUTF("UserName: " + _userName);
            while (true) {
                String msg = (String) in.readUTF();
                if (msg != null) {
                    String[] words = msg.split(":");
                    System.out.println("WORD 0: " + words[0] + " WORD 1: " + words[1]);
                    AnswerActivity.runOnUI(new Runnable() {
                        public void run() {
                            AnswerActivity.sender.setText(words[0]);
                            AnswerActivity.enigma.setText(words[1]);
                        }
                    });
                }
            }

        } catch (UnknownHostException e) {
            System.out.println("HostException Client: "+e);
            System.exit(1);
        } catch  (IOException e) {
            System.out.println("IOException Client: "+e);
            System.exit(1);
        }

    }

    public void actionPerformed(EditText enigma, EditText receiver, EditText rightAnswer){
        System.out.println("ACTION_PERFORMED");
        try {
            out.writeUTF("Enigma: \"" + enigma.getText().toString() + "\" ; Right answer: \"" + rightAnswer.getText().toString() + "\" to " + receiver.getText().toString());
        } catch (Exception e) {
            System.out.println("Exception ActPerf : " + e);
            System.exit(-1);
        }
    }

    @Override
    public int describeContents() {
        return 0;
    }

    @Override
    public void writeToParcel(Parcel parcel, int i) {
        parcel.writeString(_userName);
    }

}
