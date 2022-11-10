/**
 * @file example.cpp
 *
 * @author Philipp Jeske <philipp.jeske@koenig-bauer.com>
 * @copyright 2022 Koenig & Bauer Coding GmbH
 *
 * SPDX-License-Identifier: MIT
 */

#include <cstdlib>

#include "liba/demo.h"

int main()
{
   if (theAnswer() == 42)
   {
      return EXIT_SUCCESS;
   }
   else
   {
      return EXIT_FAILURE;
   }
}