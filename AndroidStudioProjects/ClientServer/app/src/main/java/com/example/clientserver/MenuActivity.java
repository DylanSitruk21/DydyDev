package com.example.clientserver;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;

public class MenuActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_menu);

        //Intent intent = getIntent();
        //String userName = intent.getStringExtra("userName");

        Button questionButton = (Button)findViewById(R.id.questionButton);
        questionButton.setOnClickListener((view)->{

            Intent enigmaIntent = new Intent(MenuActivity.this, EnigmaActivity.class);
            //enigmaIntent.putExtra("userName", userName);
            startActivity(enigmaIntent);

        });

        Button answerButton = (Button)findViewById(R.id.answerButton);
        answerButton.setOnClickListener((view)->{
            Intent answerIntent = new Intent(MenuActivity.this, AnswerActivity.class);
            startActivity(answerIntent);

        });
    }
}