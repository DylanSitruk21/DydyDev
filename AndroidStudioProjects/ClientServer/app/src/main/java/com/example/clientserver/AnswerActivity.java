package com.example.clientserver;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;
import android.os.Looper;
import android.widget.ImageButton;
import android.widget.TextView;

import java.text.BreakIterator;

public class AnswerActivity extends AppCompatActivity {

    public static TextView sender;
    public static TextView enigma;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_answer);

        enigma = (TextView)findViewById(R.id.newEnigma);
        sender = (TextView)findViewById(R.id.sender);

        ImageButton backToMenu = (ImageButton)findViewById(R.id.backToMenu1);
        backToMenu.setOnClickListener((view) ->{
            Intent menuIntent = new Intent(AnswerActivity.this, MenuActivity.class);
            startActivity(menuIntent);
        });



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