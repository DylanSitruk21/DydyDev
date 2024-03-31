package com.example.clientserver;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;
import android.os.Looper;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.TextView;

public class EnigmaActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_enigma);

        //Intent intent = getIntent();
        //String userName = intent.getStringExtra("userName");

        EditText enigma = (EditText) findViewById(R.id.enigma);
        enigma.setOnClickListener((view) -> {enigma.setText("");});

        EditText receiver = (EditText) findViewById(R.id.receiver);
        receiver.setOnClickListener((view) -> {receiver.setText("");});

        EditText rightAnswer = (EditText) findViewById(R.id.rightAnswer);
        rightAnswer.setOnClickListener((view) -> {rightAnswer.setText("");});

        Button sendButton = (Button)findViewById(R.id.sendButton);
        sendButton.setOnClickListener((view)->{
            System.out.println("SEND BUTTON "+ MainActivity.client._userName);
            actionPerformedThread apThread = new actionPerformedThread(MainActivity.client, enigma, receiver, rightAnswer);
            apThread.start();
            try {
                apThread.join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            enigma.setText("");
            receiver.setText("");
            rightAnswer.setText("");
        });

        ImageButton backToMenu = (ImageButton)findViewById(R.id.backToMenu2);
        backToMenu.setOnClickListener((view) ->{
            Intent menuIntent = new Intent(EnigmaActivity.this, MenuActivity.class);
            startActivity(menuIntent);
        });
    }

    class actionPerformedThread extends Thread {
        Client client;
        EditText message;
        EditText receiver;
        EditText rightAnswer;
        actionPerformedThread(Client client, EditText message, EditText receiver, EditText rightAnswer){
            this.client = client;
            this.message = message;
            this.receiver = receiver;
            this.rightAnswer = rightAnswer;
        }
        public void run() {
            client.actionPerformed(message, receiver, rightAnswer);
        }
    }

    public static Handler UIHandler;
    static
    {
        UIHandler = new Handler(Looper.getMainLooper());
    }
    public static void runOnUI(Runnable runnable) {
        UIHandler.post(runnable);
    }
}