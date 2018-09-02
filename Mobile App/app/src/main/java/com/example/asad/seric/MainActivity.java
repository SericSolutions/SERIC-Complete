package com.example.asad.seric;

import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.content.Context;
import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.media.RingtoneManager;
import android.net.Uri;
import android.os.Build;
import android.support.v4.app.NotificationCompat;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import com.google.firebase.iid.FirebaseInstanceId;
import com.google.firebase.messaging.FirebaseMessagingService;
import com.squareup.picasso.Picasso;

import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.Set;

public class MainActivity extends AppCompatActivity {

    String DTOKEN = MyFirebaseMessagingService.DTOKEN;
    private static final String channelId = "leakcanary";
    final String TAG = "FINALTAG";
    ImageView iv;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        iv = findViewById(R.id.IV);

        Log.d(TAG, FirebaseInstanceId.getInstance().getToken());
        Intent intent = getIntent();

        if (intent != null) {
            Bundle b = intent.getExtras();
            if (b != null) {
                showImage(b);
                Set<String> keys = b.keySet();
                for (String key : keys) {
                    Log.d(TAG, "Bundle Contains: key=" + key);
                }
            } else {
                Log.w(TAG, "onCreate: BUNDLE is null");
            }
        } else {
            Log.w(TAG, "onCreate: INTENT is null");
        }

    }

    void showImage(Bundle b) {
        Log.d(TAG, b.getString("Picture"));
        Picasso.get()
                .load(b.getString("Picture"))
                .placeholder(R.drawable.progress_animation)
                .into(iv);
    }

}
