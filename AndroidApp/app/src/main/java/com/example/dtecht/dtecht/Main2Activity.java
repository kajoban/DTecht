package com.example.dtecht.dtecht;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.TextSwitcher;
import android.view.Gravity;
import android.view.View;
import android.widget.TextView;
import android.widget.ViewSwitcher;
import android.graphics.Color;
import android.widget.Button;



public class Main2Activity extends AppCompatActivity {
    int nowText = -1;
    String myText[] = {"Status: You are too close to an object", "Status: You have hot an object", "Status: Someone has hit any object"};

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);

        Button button= (Button)findViewById(R.id.button);
        final TextSwitcher text = (TextSwitcher) findViewById(R.id.textView3);

        text.setFactory(new ViewSwitcher.ViewFactory() {
            @Override
            public View makeView() {
                TextView myText = new TextView(Main2Activity.this);
                myText.setGravity(Gravity.TOP | Gravity.CENTER_HORIZONTAL);
                myText.setTextColor(Color.RED);
                return myText;
            }
        });

        button.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                nowText++;
                text.setText(myText[nowText]);
            }
        });
    }


}
