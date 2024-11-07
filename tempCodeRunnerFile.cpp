#include <stdio.h>
#include <stdlib.h>
#include <string.h>


// LRT2 Stations
char *lrt2[] = {
    "Recto", "Legarda", "Pureza", "V.Mapa", "J.Ruiz",
    "Gilmore", "Betty Go-Belmonte", "Cubao",  "Anonas", "Katipunan",
    "Santolan", "Marikina-Pasig", "Antipolo"
};

// LRT1 Stations
char *lrt1[] = {
    "Roosevelt", "Balintawak", "Monumento", "5th Avenue",
    "R.Papa", "Abad Santos", "Blumentritt", "Tayuman",
    "Bambang", "Doroteo Jose", "Carriedo", "Central Terminal",
    "United Nations", "Pedro Gil", "Quirino", "Vito Cruz",
    "Gil Puyat", "Libertad", "EDSA", "Baclaran"
};

// MRT3 Stations
char *mrt3[] = {
    "North Avenue", "Quezon Avenue", "GMA Kamuning", "Araneta Cubao",
    "Santolan Annapolis", "Ortigas", "Shaw Blvd", "Boni Avenue",
    "Guadalupe", "Buendia", "Ayala", "Magallanes",
    "Taft Avenue"
};


// Fare Matrices for LRT2, LRT1, and MRT3
int fares2[13][13] = {
    {0, 15, 20, 20, 20, 25, 25, 25, 25, 30, 30, 35, 35}, // Recto
    {15, 0, 15, 20, 20, 20, 25, 25, 25, 25, 30, 30, 35}, // Legarda
    {20, 15, 0, 15, 20, 20, 20, 20, 25, 25, 30, 30, 30}, // Pureza
    {20, 20, 15, 0, 15, 20, 20, 20, 20, 25, 25, 30, 30}, // V.Mapa
    {20, 20, 20, 15, 0, 15, 20, 20, 20, 20, 25, 25, 30}, // J.Ruiz
    {25, 20, 20, 20, 15, 0, 15, 20, 20, 20, 25, 25, 30}, // Gilmore
    {25, 25, 20, 20, 20, 15, 0, 15, 20, 20, 20, 25, 25}, // Betty Go Belmonte
    {25, 25, 20, 20, 20, 20, 15, 0, 15, 20, 20, 25, 25}, // Araneta Center Cubao
    {25, 25, 25, 20, 20, 20, 20, 15, 0, 15, 20, 20, 25}, // Anonas
    {30, 25, 25, 25, 20, 20, 20, 20, 15, 0, 20, 20, 25}, // Katipunan
    {30, 30, 30, 25, 25, 25, 20, 20, 20, 20, 0, 15, 20}, // Santolan
    {35, 30, 30, 30, 25, 25, 25, 25, 20, 20, 15, 0, 20}, // Marikina-Pasig
    {35, 35, 30, 30, 30, 30, 25, 25, 25, 25, 20, 20, 0}  // Antipolo
};

int fares1[20][20] = {
    {0,  15, 20, 20, 20, 25, 25, 25, 25, 30,
     30, 35, 35, 35, 35, 35, 40, 40, 40, 45}, // Roosevelt
    {15, 0,  15, 20, 20, 20, 25, 25, 25, 30,
     30, 35, 35, 35, 35, 40, 40, 40, 45, 45}, // Balintawak
    {20, 15, 0,  15, 20, 20, 20, 25, 25, 30,
     30, 35, 35, 35, 40, 40, 40, 45, 45, 50}, // Monumento
    {20, 20, 15, 0,  15, 20, 20, 25, 30, 30,
     30, 35, 35, 35, 40, 40, 45, 45, 50, 50}, // 5th Avenue
    {20, 20, 20, 15, 0,  15, 20, 25, 30, 30,
     35, 35, 35, 40, 40, 45, 45, 50, 50, 55}, // R.Papa
    {25, 20, 20, 20, 15, 0,  15, 20, 25, 30,
     30, 35, 35, 40, 45, 45, 50, 50, 55, 55}, // Abad Santos
    {25, 25, 20, 20, 20, 15, 0,  15, 25, 30,
     35, 35, 40, 45, 45, 50, 50, 55, 55, 60}, // Blumentritt
    {25, 25, 25, 25, 25, 20, 15, 0,  15, 25,
     35, 35, 40, 45, 50, 50, 55, 55, 60, 60}, // Tayuman
    {25, 25, 25, 30, 30, 25, 25, 15, 0,  15,
     25, 30, 40, 45, 45, 50, 55, 60, 60, 65}, // Bambang
    {30, 30, 30, 30, 30, 30, 30, 25, 15, 0,
     15, 25, 30, 40, 45, 50, 55, 55, 60, 65}, // Doroteo Jose
    {30, 30, 30, 30, 35, 30, 35, 35, 25, 15,
     0,  15, 25, 30, 40, 45, 50, 55, 55, 60}, // Carriedo
    {35, 35, 35, 35, 35, 35, 35, 35, 30, 25,
     15, 0,  15, 25, 30, 40, 45, 50, 55, 60}, // Central Terminal
    {35, 35, 35, 35, 35, 35, 40, 40, 40, 30,
     25, 15, 0,  15, 25, 30, 40, 45, 50, 55}, // United Nations
    {35, 35, 35, 35, 40, 40, 45, 45, 45, 40,
     30, 25, 15, 0,  15, 25, 30, 40, 45, 50}, // Pedro Gil
    {35, 35, 40, 40, 40, 45, 45, 50, 45, 45,
     40, 30, 25, 15, 0,  15, 25, 30, 40, 45}, // Quirino
    {35, 40, 40, 40, 45, 45, 50, 50, 50, 50,
     45, 40, 30, 25, 15, 0,  15, 25, 30, 40}, // Vito Cruz
    {40, 40, 40, 45, 45, 50, 50, 55, 55, 55,
     50, 45, 40, 30, 25, 15, 0,  15, 25, 30}, // Gil Puyat
    {40, 40, 45, 45, 50, 50, 55, 55, 60, 55,
     55, 50, 45, 40, 30, 25, 15, 0,  15, 25}, // Libertad
    {40, 45, 45, 50, 50, 55, 55, 60, 60, 60,
     55, 55, 50, 45, 40, 30, 25, 15, 0,  15}, // EDSA
    {45, 45, 50, 50, 55, 55, 60, 60, 65, 65,
     60, 60, 55, 50, 45, 40, 30, 25, 15, 0} // Baclaran
};

int mrt3trainChart[13][13] = {
    {0, 13, 13, 16, 16, 20, 20, 20, 24, 24, 24, 28, 28}, // North Ave
    {13, 0, 13, 13, 16, 16, 20, 20, 20, 24, 24, 24, 28}, // Quezon Ave
    {13, 13, 0, 13, 13, 16, 16, 20, 20, 20, 24, 24, 24}, // GMA Kamuning
    {16, 13, 13, 0, 13, 13, 16, 16, 20, 20, 20, 24, 24}, // Araneta-Cubao
    {16, 16, 13, 13, 0, 13, 13, 16, 16, 20, 20, 20, 24}, // Santolan-Annapolis
    {20, 16, 16, 13, 13, 0, 13, 13, 16, 16, 20, 20, 20}, // Ortigas
    {20, 20, 16, 16, 13, 13, 0, 13, 13, 16, 16, 20, 20}, // Shaw Blvd.
    {20, 20, 20, 16, 16, 13, 13, 0, 13, 13, 16, 16, 20}, // Boni
    {24, 20, 20, 20, 16, 16, 13, 13, 0, 13, 13, 16, 16}, // Guadalupe
    {24, 24, 20, 20, 20, 16, 16, 13, 13, 0, 13, 13, 16}, // Buendia
    {24, 24, 24, 20, 20, 20, 16, 16, 13, 13, 0, 13, 13}, // Ayala
    {28, 24, 24, 24, 20, 20, 20, 16, 16, 13, 13, 0, 13}, // Magallanes
    {28, 28, 24, 24, 24, 20, 20, 20, 16, 16, 13, 13, 0}  // Taft Ave
};

float lrt2_distances[] = {
          1.05, 1.38, 1.35, 1.23,
          0.92, 1.07, 1.16, 1.43,
          0.95, 1.97, 1.79, 2.23
        };

        float lrt1_distances[] = {
          1.87, 2.25, 1.08, 0.95, 0.66,
          0.92, 0.67, 0.61, 0.64, 0.68,
          0.72, 1.21, 0.75, 0.79, 0.82,
          1.06, 0.73, 1.01, 0.58
        };

        float mrt3_distances[] = {
          1.22, 0.94, 1.85, 1.45,
          2.31, 0.77, 0.98, 0.77,
          1.83, 0.88, 1.19, 1.89
        };

// Discount for Single Journey Ticket
float getDiscount(char cardType) {
  switch (cardType) {
  case 'S':case 's':
    return 0.2; // Student
  case 'P':case 'p':
    return 0.3; // PWD/Senior
   case 'R':case 'r':
    return 0.0; // Regular
     default:
   return -1;
  }
}
//Discount for Beep Card Only
 float getDiscount2(char cardType2) {
  switch (cardType2) {
  case 'P':case 'p':
    return 0.3; // PWD/Senior
    case 'R':case 'r':
    return 0.0; // Regular
    default:
   return -1;
  }
}

// Function to print LRT/MRT stations
void printStations(char *stations[], int count) {
  for (int i = 0; i < count; i++) {
    printf("[%d] %s\n", i, stations[i]);
  }
}

float calculateDistance(float distances[], int initial, int destination) {
  float count = 0;
  int index = initial; // index for the for loop

  for (;;) {
    if (index == destination) {
      break;
    }
    if (initial < destination) {
      count += distances[index];
      index += 1;
    } else {
      count += distances[index - 1];
      index -= 1;
    }
  }
  return count;
}



int main(){
    char cardType;
    char cardType2;
    float discount, kilometer, totalDistance = 0;
    int totalFare = 0, rideCount = 0, totalStations = 0;
    char choice[10];
    char sorc[10] = "";
    int validInput = 0;
    int current, destination, total, fare, lrtChoice, distance;
     char continueRide = 'Y' || 'y';

    printf("Good Day, Boss!\n");

    printf("\nWhich Train line are you riding? (1 for LRT1, 2 for LRT2, 3 for MRT3): ");
    scanf("%d", &lrtChoice);

    // Start a loop for input validation
    while (!validInput) {
        printf("Enter Card ((Single) for Single Journey and (Beep) for Beep Card): ");
        scanf("%s", sorc);

        if(strcmp(sorc, "Beep") == 0 || strcmp(sorc, "beep") == 0){ 
            printf("Enter card type for discount (R for Regular, or P for PWD/Senior): ");
            scanf(" %c", &cardType2);
            discount = getDiscount2(cardType2);
            if (discount == -1) {
                printf("Invalid input! Please try again.\n");
            } else {
                validInput = 1;  // Exit loop on valid input
            }
        }
        else if(strcmp(sorc, "Single") == 0 || strcmp(sorc, "single") == 0){
            printf("Enter card type for discount (R for Regular, S for Student, P for PWD/Senior): ");
            scanf(" %c", &cardType);
            discount = getDiscount(cardType);
            if (discount == -1) {
                printf("Invalid input! Please try again.\n");
            } else {
                validInput = 1;  // Exit loop on valid input
            }
        }
        else{
            printf("\nInvalid Input! Please Try Again!\n\n");
        }
    }

    // Display stations based on the train line choice
    if (lrtChoice == 3) {
        printf("\nMRT3 Stations:\n");
        printStations(mrt3, 13);
    } else if (lrtChoice == 2) {
        printf("\nLRT2 Stations:\n");
        printStations(lrt2, 13);
    } else {
        printf("\nLRT1 Stations:\n");
        printStations(lrt1, 20);
    }

    printf("\nEnter the number of your initial station: ");
    scanf("%d", &current);

    do {
    if (rideCount == 0) {
        printf("Enter the number of your destination: ");
    } else {
        printf("Enter the number of your new final destination: ");
    }
    
    scanf("%s", choice);
    destination = atoi(choice);

    // Calculate fare and distance based on the train line choice
    if (lrtChoice == 3) {
        fare = mrt3trainChart[current][destination];
        kilometer = calculateDistance(mrt3_distances, current, destination);
    } else if (lrtChoice == 2) {
        fare = fares2[current][destination];
        kilometer = calculateDistance(lrt2_distances, current, destination);
    } else {
        fare = fares1[current][destination];
        kilometer = calculateDistance(lrt1_distances, current, destination);
    }

    distance = (int)kilometer;
    total = abs(destination - current);
    totalStations += total;
    totalDistance += kilometer;

    // Apply discount
    fare -= fare * discount;

    // Add fare to total fare
    totalFare += fare;
    rideCount++;

    // Output fare and distance for the current ride
    printf("Fare for this ride: %d pesos\n", fare);
    printf("Distance traveled in this ride: %.2f km\n", kilometer);
    printf("Total stations passed: %d\n", total);

    current = destination;

    printf("\nDo you want to ride again? Type 'Y' or 'y' to continue, or press any other key to stop.");
    scanf("%s", choice);

    if(continueRide != 'Y' && continueRide != 'y') {
    break;
}
    

} while (1);

    // Display total fare, rides, total distance, and stations
    printf("\nTotal rides: %d\nTotal fare: %d pesos\n", rideCount, totalFare);
    printf("Total distance traveled: %.2f km\n", totalDistance);
    printf("Total stations passed: %d\n", totalStations);
    printf("Thank you for using our service. We hope to see you again soon!\n");

    return 0;
}