#include "OverlaySpinner.h"

#include "Utils.h"

void OverlaySpinnerTimer::timerCallback() {
  if (overlaySpinner) {
    auto lsp = overlaySpinner->spinnerImage.get();
    const auto& lspImg = overlaySpinner->spinnerImages;

    // change image
    i = (i + 1) % lspImg.size();
    lsp->setImage(lspImg[i]);

    // check timeout
    t += getTimerInterval();
    if (t > timeout) {
      t = 0;
      overlaySpinner->setVisible(false);
      stopTimer();
    }
  }
}

OverlaySpinner::OverlaySpinner() : overlaySpinnerTimer(this) {
  //launchSpinnerTimer.launcherComponent = this;
  Array<String> spinnerImgPaths;
  spinnerImgPaths.add("wait0.png");
  spinnerImgPaths.add("wait1.png");
  spinnerImgPaths.add("wait2.png");
  spinnerImgPaths.add("wait3.png");
  spinnerImgPaths.add("wait4.png");
  spinnerImgPaths.add("wait5.png");
  spinnerImgPaths.add("wait6.png");
  spinnerImgPaths.add("wait7.png");
  for(auto& path : spinnerImgPaths) {
    auto image = createImageFromFile(assetFile(path));
    spinnerImages.add(image);
  }

  spinnerImage = new ImageComponent();
  spinnerImage->setImage(spinnerImages[0], RectanglePlacement::centred);
  addAndMakeVisible(spinnerImage);
}

OverlaySpinner::~OverlaySpinner() {
  overlaySpinnerTimer.stopTimer();
}

void OverlaySpinner::paint(Graphics &g) {
  g.fillAll(Colour((uint8)254, 255, 255, (uint8)201));
}

void OverlaySpinner::resized() {
  auto bounds = getLocalBounds();
  int spinnerSize = bounds.getHeight() / 10;
  spinnerImage->setBounds(
    (bounds.getWidth() - spinnerSize) / 2,
    (bounds.getHeight() - spinnerSize) / 2,
    spinnerSize,
    spinnerSize
  );
}

void OverlaySpinner::setVisible(bool shouldBeVisible) {
  DBG("Show spinner");
  Component::setVisible(shouldBeVisible);

  if (shouldBeVisible) {
    overlaySpinnerTimer.startTimer(500);
  } else {
    overlaySpinnerTimer.stopTimer();
  }
}
