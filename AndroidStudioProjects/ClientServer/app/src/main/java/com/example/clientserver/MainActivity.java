package com.example.clientserver;

import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    public static Client client;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        EditText userName = (EditText) findViewById(R.id.userName);
        userName.setOnClickListener((view) -> {userName.setText("");});

        Button userButton = (Button)findViewById(R.id.userButton);
        userButton.setOnClickListener((view)->{
            System.out.println("USER BUTTON " +  userName.getText().toString());

            client = new Client(userName.getText().toString());
            clientRunnable cRunnable = new clientRunnable(client);
            new Thread(cRunnable).start();

            Intent intent = new Intent(MainActivity.this, MenuActivity.class);
            //intent.putExtra("userName", (String) userName.getText().toString());
            startActivity(intent);
        });
    }


    class clientRunnable implements Runnable {
        Client client;
        clientRunnable(Client client) {
            this.client = client;
        }

        public void run() {
            client.listenSocket();
        }
    }
}
