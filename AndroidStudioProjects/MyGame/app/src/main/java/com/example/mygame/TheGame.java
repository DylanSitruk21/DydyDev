package com.example.mygame;

import androidx.appcompat.app.AppCompatActivity;
import androidx.constraintlayout.widget.ConstraintLayout;

import android.graphics.Color;
import android.os.Bundle;
import android.text.Editable;
import android.text.TextWatcher;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class TheGame extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_the_game);


        int unicode = 0x1F600;
        TextView emojiText = (TextView) findViewById(R.id.emojiText);
        String emoji = new String(Character.toChars(unicode));
        emojiText.setText(emoji+emoji);
        emojiText.setTextSize(30);

        final EditText answerText = (EditText) findViewById(R.id.answerText);
        answerText.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                answerText.setText("");
            }
        });

        Button validBtn = (Button) findViewById(R.id.validBtn);
        validBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                EditText answerText = (EditText) findViewById(R.id.answerText);
                TextView resultText = (TextView) findViewById(R.id.resultText);
                ConstraintLayout background2 = (ConstraintLayout) findViewById(R.id.background2);
                if(answerText.getText().toString().equalsIgnoreCase("smile")){
                    resultText.setText("Good !!");
                    resultText.setTextSize(40);
                    background2.setBackgroundColor(Color.GREEN);
                }else {
                    resultText.setText("Oh nooo..");
                    resultText.setTextSize(40);
                    background2.setBackgroundColor(Color.RED);
                }

            }
        });
    }
}