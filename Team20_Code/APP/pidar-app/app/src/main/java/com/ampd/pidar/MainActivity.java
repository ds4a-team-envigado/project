package com.ampd.pidar;

import android.Manifest;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.net.Uri;
import android.os.Bundle;

import com.ampd.pidar.geolocation.GeolocatorService;

import com.ampd.pidar.geolocation.Municipality;
import com.github.nikartm.button.FitButton;
import com.google.android.gms.location.FusedLocationProviderClient;
import com.google.android.gms.location.LocationServices;
import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.android.material.snackbar.Snackbar;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;

import android.provider.Settings;
import android.text.TextUtils;
import android.view.View;

import java.util.Locale;


import android.widget.TextView;
import android.widget.Toast;

import org.jetbrains.annotations.NotNull;

import timber.log.Timber;


public class MainActivity extends AppCompatActivity implements OnMapReadyCallback, GeolocatorService.ResponseActionDelegate {

    private static final String TAG = MainActivity.class.getSimpleName();

    private static final int REQUEST_PERMISSIONS_REQUEST_CODE = 34;
    private static final float LOCATION_REFRESH_DISTANCE = 500;
    private static final long LOCATION_REFRESH_TIME = 5000;
    private FusedLocationProviderClient mFusedLocationClient;
    protected Location mLastLocation;
    private GoogleMap googleMap;
    private double latitude = 4.5709;
    private double longitude = 74.2973;


    private String mLatitudeLabel;

    private TextView locationNameTextView;

    private SupportMapFragment mapFragment;

    private Municipality _municipality;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mLatitudeLabel = getResources().getString(R.string.latitude_label);

        locationNameTextView = (TextView) findViewById((R.id.location_name));
        // mLongitudeText = (TextView) findViewById((R.id.longitude_text));


        if (BuildConfig.DEBUG) {
            Timber.plant(new Timber.DebugTree());
        }

        FitButton yesButton = findViewById(R.id.yes_answer);
        FitButton noButton = findViewById(R.id.no_answer);
        yesButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                showSurvey();
            }
        });


        noButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                showMunicipalitySelection();
            }


        });


        mFusedLocationClient = LocationServices.getFusedLocationProviderClient(this);
    }

    private void showSurvey() {

        if(_municipality == null){
            handleNoDepartment();
            return;
        }


        if(TextUtils.isEmpty(_municipality.getCode())){
            handleNoDepartment();
            return;
        }


        PidarForm.getInstance().setDepartment(_municipality.getCode());

        final Intent intent = new Intent(this, PidarSurveyActivity.class);
        startActivity(intent);

    }

    private void handleNoDepartment(){
        Toast.makeText(this, getString(R.string.error_department), Toast.LENGTH_LONG).show();
        showMunicipalitySelection();

    }

    private void showMunicipalitySelection() {
        final Intent intent = new Intent(this, MunicipalitySelectionActivity.class);
        startActivity(intent);
    }

    @Override
    public void onStart() {
        super.onStart();

        if (!checkPermissions()) {
            requestPermissions();
        } else {
            getLastLocation();
        }
    }

    private void showLocationName(){
        GeolocatorService geolocatorService = new GeolocatorService();
        geolocatorService.sendRequest(this, latitude, longitude);
    }




    /**
     * Provides a simple way of getting a device's location and is well suited for
     * applications that do not require a fine-grained location and that do not need location
     * updates. Gets the best and most recent location currently available, which may be null
     * in rare cases when a location is not available.
     * <p>
     * Note: this method should be called after location permission has been granted.
     */
    @SuppressWarnings("MissingPermission")
    private void getLastLocation() {
        mFusedLocationClient.getLastLocation()
                .addOnCompleteListener(this, new OnCompleteListener<Location>() {
                    @Override
                    public void onComplete(@NonNull Task<Location> task) {
                        if (task.isSuccessful() && task.getResult() != null) {
                            mLastLocation = task.getResult();

                            locationNameTextView.setText(String.format(Locale.ENGLISH, "%s: %f",
                                    mLatitudeLabel,
                                    mLastLocation.getLatitude()));

                            latitude = mLastLocation.getLatitude();
                            longitude = mLastLocation.getLongitude();

                            setMapLocation();

                        } else {

                            showSnackbar(getString(R.string.no_location_detected));
                        }
                    }
                });
    }

    private void showSnackbar(final String text) {

    }

    private void setMapLocation() {
        mapFragment = (SupportMapFragment) getSupportFragmentManager().findFragmentById(R.id.map);
        assert mapFragment != null;
        mapFragment.getMapAsync(this);
    }


    private void showSnackbar(final int mainTextStringId, final int actionStringId,
                              View.OnClickListener listener) {
        Snackbar.make(findViewById(android.R.id.content),
                getString(mainTextStringId),
                Snackbar.LENGTH_INDEFINITE)
                .setAction(getString(actionStringId), listener).show();
    }

    private boolean checkPermissions() {
        int permissionState = ActivityCompat.checkSelfPermission(this,
                Manifest.permission.ACCESS_FINE_LOCATION);
        return permissionState == PackageManager.PERMISSION_GRANTED;
    }

    private void startLocationPermissionRequest() {
        ActivityCompat.requestPermissions(MainActivity.this,
                new String[]{Manifest.permission.ACCESS_FINE_LOCATION},
                REQUEST_PERMISSIONS_REQUEST_CODE);
    }

    private void requestPermissions() {
        boolean shouldProvideRationale =
                ActivityCompat.shouldShowRequestPermissionRationale(this,
                        Manifest.permission.ACCESS_FINE_LOCATION);

        // Provide an additional rationale to the user. This would happen if the user denied the
        // request previously, but didn't check the "Don't ask again" checkbox.
        if (shouldProvideRationale) {

            showSnackbar(R.string.permission_rationale, android.R.string.ok,
                    new View.OnClickListener() {
                        @Override
                        public void onClick(View view) {
                            // Request permission
                            startLocationPermissionRequest();
                        }
                    });

        } else {

            startLocationPermissionRequest();
        }
    }

    /**
     * Callback received when a permissions request has been completed.
     */
    @Override
    public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions,
                                           @NonNull int[] grantResults) {

        if (requestCode == REQUEST_PERMISSIONS_REQUEST_CODE) {
            if (grantResults.length <= 0) {

            } else if (grantResults[0] == PackageManager.PERMISSION_GRANTED) {
                setupLocationListener();
                getLastLocation();
            } else {

                showSnackbar(R.string.permission_denied_explanation, R.string.settings,
                        new View.OnClickListener() {
                            @Override
                            public void onClick(View view) {
                                // Build intent that displays the App settings screen.
                                Intent intent = new Intent();
                                intent.setAction(
                                        Settings.ACTION_APPLICATION_DETAILS_SETTINGS);
                                Uri uri = Uri.fromParts("package",
                                        BuildConfig.APPLICATION_ID, null);
                                intent.setData(uri);
                                intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
                                startActivity(intent);
                            }
                        });
            }
        }
    }

    @Override
    public void onMapReady(GoogleMap googleMap) {
        Timber.d("onMapReadyT %f", latitude);
        this.googleMap = googleMap;
        centerMap();
        showLocationName();
    }


    private void centerMap(){
       // LatLng currentLocation = new LatLng(latitude, longitude);
        LatLng locationShift = new LatLng(latitude - 0.19, longitude);
        googleMap.moveCamera(CameraUpdateFactory.newLatLng(locationShift));
        googleMap.animateCamera(CameraUpdateFactory.zoomTo(10.0f));
    }

    private LocationManager mLocationManager;

    private void setupLocationListener() {
        Timber.e("setupLocationListener");
        mLocationManager = (LocationManager) getSystemService(LOCATION_SERVICE);

        if (ActivityCompat.checkSelfPermission(this, Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED && ActivityCompat.checkSelfPermission(this, Manifest.permission.ACCESS_COARSE_LOCATION) != PackageManager.PERMISSION_GRANTED) {

            return;
        }
        mLocationManager.requestLocationUpdates(LocationManager.NETWORK_PROVIDER, LOCATION_REFRESH_TIME,
                LOCATION_REFRESH_DISTANCE, mLocationListener);
    }

    private final LocationListener mLocationListener = new LocationListener() {
        @Override
        public void onLocationChanged(final Location location) {
            Timber.e("LocationListener onLocationChanged");
            centerMap();
        }

        @Override
        public void onStatusChanged(String provider, int status, Bundle extras) {

        }

        @Override
        public void onProviderEnabled(String provider) {

        }

        @Override
        public void onProviderDisabled(String provider) {

        }
    };


    @Override
    public void didNotSuccessfully(@NotNull String error) {
        showSnackbar(getString(R.string.no_location_detected));
        //showMunicipalitySelection();
    }

    @Override
    public void didSuccessfully(@NotNull Municipality municipality) {
        this._municipality = municipality;
        String locationName = "Departamento de: "+municipality.getDepartment()+ ", municipio "+municipality.getName();

        locationNameTextView.setText(locationName);
    }
}
